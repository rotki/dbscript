import argparse

from pysqlcipher3 import dbapi2 as sqlcipher

from config import default_data_directory

SCRIPT = """
DROP TABLE IF EXISTS eth2_deposits;
DELETE from used_query_ranges WHERE name LIKE "eth2_deposits_%";
INSERT OR REPLACE INTO settings(name, value) VALUES('version', '22');
"""


def read_args():
    parser = argparse.ArgumentParser(
        prog='Rotki DB helper',
        description='A tool to help get your DB unstuck',
    )
    parser.add_argument(
        '--data-dir',
        default=None,
        help='The path to rotki data directory',
    )
    parser.add_argument(
        '--user',
        help='The user whose DB to change',
    )
    parser.add_argument(
        '--password',
        help='The password of the users DB',
    )
    args = parser.parse_args()

    if args.data_dir:
        data_dir = args.data_dir
    else:
        data_dir = default_data_directory()

    user = args.user
    password = args.password

    return data_dir, user, password

def main(data_dir, user, password):
    fullpath = data_dir / user / 'rotkehlchen.db'
    conn = sqlcipher.connect(str(fullpath))
    conn.text_factory = str
    script = f'PRAGMA key="{password}";'
    conn.executescript(script)
    conn.execute('PRAGMA foreign_keys=ON')
    conn.executescript(SCRIPT)


if __name__ == "__main__":
    data_dir, user, password = read_args()
    main(data_dir, user, password)
