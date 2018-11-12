# catchpoint_query_tools
--------

usage: tst.py [-h] [-k [KEY]] [-s [SECRET]] [-v [VERSION]] [-sk [SORT_KEY]]

calls catchpoint api returning sorted array of test_ids grouped by type

optional arguments:
  -h, --help            show this help message and exit
  -k [KEY], --key [KEY]
                        <catchpoint REST_API KEY>
  -s [SECRET], --secret [SECRET]
                        <catchpoint REST_API SECRET>
  -v [VERSION], --version [VERSION]
                        <url version "1" or "2">
  -sk [SORT_KEY], --sort-key [SORT_KEY]
                        <sort by test_type - "id" or "name"> 
