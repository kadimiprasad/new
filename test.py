"""import unittest module"""
import unittest
import log


class TestStringMethods(unittest.TestCase):
    """Test_methods"""

    def test_logarithm(self):
        """Test_valid_input"""
        self.assertEqual(log.logarithm(100000), 5.0)
    # test_type_of_variable

    def test_logarithm2(self):
        """Test_for_negative"""
        self.assertRaises(ValueError)
    # # test_for_negative_number

    def test_logarithm3(self):
        """Test_for_invalid_type"""
        self.assertRaises(TypeError)
