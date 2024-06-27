import unittest
from models.bandit_model import EpsilonGreedyBandit

class TestEpsilonGreedyBandit(unittest.TestCase):

    def test_select_arm(self):
        bandit = EpsilonGreedyBandit(n_arms=10, epsilon=0.1)
        arm = bandit.select_arm()
        self.assertIn(arm, range(10))
    
    def test_update(self):
        bandit = EpsilonGreedyBandit(n_arms=10, epsilon=0.1)
        bandit.update(chosen_arm=0, reward=1.0)
        self.assertEqual(bandit.counts[0], 1)
        self.assertAlmostEqual(bandit.values[0], 1.0)

if __name__ == '__main__':
    unittest.main()
