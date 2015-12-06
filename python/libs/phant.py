import urllib
import urllib3
import sqlite3
import csv

def writer_factory(endpoint, *plain, **converters):
    for p in plain:
        converters[p] = lambda x: x
    def committer(**values):
        converted = {}
        if set(converters.keys()) ^ set(values.keys()):
            raise TypeError('Value mismatch (expected: %s)' % (
                ', '.join(converters.keys())
            ))
        for k, v in values.items():
            try:
                converted[k] = converters[k](v)
            except ValueError:
                raise ValueError(
                    'Parameter "%s" can not be converted with "%s"' % (
                    k, converters[k].__name__
                ))
        url = endpoint + '&' + urllib.parse.urlencode(converted)
        http = urllib3.PoolManager()
        return bool(int(http.urlopen('POST', url).read(1)))
    return committer

def _safe(field):
    if set(field) & set('\\\'\x00"'):
        raise ValueError('Invalid field name: ' + field)
    field = field.encode("utf-8", 'strict').decode("utf-8")
    return '"%s"' % field

def reader(url, name, conn=None, **converters):
    if conn is None:
        conn = sqlite3.connect(':memory:')
    http = urllib3.PoolManager()
    csv_reader = csv.DictReader(http.urlopen('GET', url + '.csv'))
    fn = csv_reader.fieldnames
    conn.execute('CREATE TABLE %s (%s)' % (
        name, ', '.join([_safe(x) for x in fn])))
    for row in csv_reader:
        values = [converters.get(key, lambda x: x)(row[key]) for key in fn]
        conn.execute('INSERT INTO "%s" VALUES (%s)' % (name,
            ', '.join(['?' for _ in fn])), values)

    return conn
