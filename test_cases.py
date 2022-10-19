"""Module with unit tests cases
Case describes:
- input string data (:data:)
- expected calculated sum (:metadata_sum:)
- expected calculated root value (:root_node_value:)
"""

cases = (
    {
        'msg': 'case number: 1',
        'data': [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2],
        'metadata_sum': 138,
        'root_node_value': 66,
    },
    {
        'msg': 'case number: 2',
        'data': [0, 0],
        'metadata_sum': 0,
        'root_node_value': 0,
    },
    {
        'msg': 'case number: 3',
        'data': [0, 3, 10, 11, 12],
        'metadata_sum': 33,
        'root_node_value': 33,
    },
    {
        'msg': 'case number: 4',
        'data': [1, 1, 0, 1, 99, 2, 1],
        'metadata_sum': 101,
        'root_node_value': 0,
    },
    {
        'msg': 'case number: 5',
        'data': [0, 1, 99],
        'metadata_sum': 99,
        'root_node_value': 99,
    },
    {
        'msg': 'case number: 6',
        'data': [1, 4, 1, 1, 1, 2, 3, 2, 1, 1, 0, 3, 6, 6, 6, 5, 0, 1, 8, 0, 3, 101, 1, 13, 2, 3, 11, 9, 77, 4, 18],
        'metadata_sum': 270,
        'root_node_value': 0,
    },
    {
        'msg': 'case number: 7',
        'data': [1, 1, 0, 2, 1, 1, 15],
        'metadata_sum': 17,
        'root_node_value': 0,
    },
    {
        'msg': 'case number: 8',
        'data': [1, 3, 0, 2, 1, 1, 0, 1, 1],
        'metadata_sum': 4,
        'root_node_value': 6,
    },
    {
        'msg': 'case number: 9',
        'data': [2, 2, 1, 3, 1, 4, 1, 2, 0, 1, 8, 3, 77, 1, 0, 0, 5, 11, 30, 69, 1, 1, 0, 2, 1, 1, 15],
        'metadata_sum': 221,
        'root_node_value': 0,
    },
    {
        'msg': 'case number: 10',
        'data': [1, 4, 1, 2, 0, 1, 100, 7, 29, 11, 0, 5, 99],
        'metadata_sum': 251,
        'root_node_value': 0,
    },
)
