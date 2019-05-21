import unittest


"""
def sample_sum(arg):
    # initialize
    total = 0

    for i in arg:
        total += i

    return total


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sample_sum([1, 2, 3]), 6, "Should be equal to 6")


if __name__ == "__main__":
    unittest.main()
    """


def function(**kwargs):
    value = kwargs
    return value


print(function(testing='one'))
print(dict(testing='one'))
