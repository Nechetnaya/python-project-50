RESULT = '{\n' \
         '  - follow: false\n' \
         '    host: hexlet.io\n' \
         '  - proxy: 123.234.53.22\n' \
         '  - timeout: 50\n' \
         '  + timeout: 20\n' \
         '  + verbose: true\n' \
         '}'

RESULT_SAME = '{\n' \
              '  host: hexlet.io\n' \
              '  timeout: 50\n' \
              '  proxy: 123.234.53.22\n' \
              '  follow: false\n' \
              '}'

RESULT_ONE_EMPTY = '{\n' \
              '  - host: hexlet.io\n' \
              '  - timeout: 50\n' \
              '  - proxy: 123.234.53.22\n' \
              '  - follow: false\n' \
              '}'

RESULT_BOTH_EMPTY = ''
