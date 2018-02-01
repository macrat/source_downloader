#!/bin/env python3

import json
import pathlib
import sys
import urllib.parse
import urllib.request


def read_map(name):
    try:
        with open(name) as f:
            data = json.load(f)

        basepath = pathlib.Path(name + '.source_downloader')
    except FileNotFoundError:
        with urllib.request.urlopen(name) as res:
            data = res.read().decode('utf-8')

        try:
            data = json.loads(data)
        except json.decoder.JSONDecodeError:
            lastline = data.splitlines()[-1]

            if 'sourceMappingURL' not in lastline:
                print('source mapping URL was not found in this script.', file=sys.stderr)
                sys.exit(2)

            url = urllib.parse.urljoin(
                name,
                '='.join(lastline.split('=')[1:]).strip(),
            )
            try:
                with urllib.request.urlopen(url) as res:
                    data = json.loads(res.read().decode('utf-8'))
            except:
                print('failed to map from URL: {}'.format(url), file=sys.stderr)
                sys.exit(2)

        url = urllib.parse.urlparse(name)
        basepath = pathlib.Path(url.netloc + url.path).parent
    except:
        print('failed to read map from file: {}'.format(name), file=sys.stderr)
        sys.exit(2)

    return data, basepath


def save_map(data, basepath):
    for fname, content in zip(data['sources'], data['sourcesContent']):
        path = (basepath / fname)
        print(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('$ ./source_downloader.py [source map file|source map url|javascript url]', file=sys.stderr)
        sys.exit(1)

    data, basepath = read_map(sys.argv[1])
    save_map(data, basepath)
