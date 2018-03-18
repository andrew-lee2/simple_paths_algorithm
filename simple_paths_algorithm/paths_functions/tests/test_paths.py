from unittest import TestCase
from ...examples import example_graph_1
from ...paths_functions import SimplePaths
from nose.tools import eq_
import networkx


class TestPath(TestCase):
    def __init__(self):
        """test class for paths_function.py"""
        super(TestPath, self).__init__()
        self.ex1_nodes, self.ex1_edges = example_graph_1()
        self.simple_path = SimplePaths(self.ex1_nodes, self.ex1_edges, 4)

    def test_get_simple_paths_result(self):
        """
        test get_simple_paths_result
        """
        results = self.simple_path.get_simple_paths_result()
        eq_(round(results.node_score[0], 2), .96)

    def test_get_node_edge_data_nodes(self):
        """
        test get_node_edge_data, nodes output
        """
        eq_(self.simple_path.nodes_df.columns[0], 'node')

    def test_get_node_edge_data_edges(self):
        """
        test get_node_edge_data, edges output
        """
        eq_(self.simple_path.edges_df.columns[0], 'node_a')

    def test_get_node_edge_lists_nodes(self):
        """
        test get_node_edge_lists, nodes output
        """
        self.assertItemsEqual(self.simple_path.node_list, [1, 2, 3, 4])

    def test_get_node_edge_lists_edges(self):
        """
        test get_node_edge_lists, edges output
        """
        eq_(self.simple_path.edge_tuple_list[0], (1, 2))

    def test_get_graph_graph(self):
        """
        test get_graph, graph output
        """
        self.assertIsInstance(self.simple_path.di_graph, networkx.digraph.DiGraph)

    def test_get_node_simple_paths(self):
        """
        test simple paths output of node 1
        """
        test_paths_list = [[1, 2], [1, 3, 2], [1, 2, 4, 3], [1, 3], [1, 2, 4], [1, 3, 2, 4]]
        paths_list = self.simple_path._get_node_simple_paths(1)
        self.assertItemsEqual(paths_list, test_paths_list)

    def test_get_node_weights(self):
        """
        test node 1 weight
        """
        weight_dict = self.simple_path._get_node_weights()
        eq_(weight_dict[1], 1 / float(3))

    def test_get_node_score(self):
        """
        test value of node 1
        """
        weight_dict = self.simple_path._get_node_weights()
        paths_list = self.simple_path._get_node_simple_paths(1)
        node_score = self.simple_path.get_node_score(paths_list, weight_dict)
        eq_(node_score, .96)

    def test_get_graph_score(self):
        """
        test score of node 1
        """
        node_scores = self.simple_path.get_graph_score()
        eq_(node_scores.node_score[0], .96)

    def test_get_graph_diameter(self):
        graph_diameter = self.simple_path.get_graph_diameter()
        eq_(graph_diameter, 4)
