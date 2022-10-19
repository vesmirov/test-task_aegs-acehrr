import unittest

from test_cases import cases

from nodes import build_tree, get_sum_of_metadata, get_root_value


class TestNodes(unittest.TestCase):
    def test_cases_metadata(self):
        for case in cases:
            with self.subTest(msg=case['msg']):
                tree, _ = build_tree(case['data'])
                self.assertEqual(
                    get_sum_of_metadata(tree),
                    case['metadata_sum'],
                )

    def test_case_root_value(self):
        for case in cases:
            with self.subTest(msg=case['msg']):
                tree, _ = build_tree(case['data'])
                self.assertEqual(
                    get_root_value(tree),
                    case['root_node_value'],
                )

