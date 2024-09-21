import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):

        wal = runner.Runner(name='wal')
        for _ in range(10):
            wal.walk()
        self.assertEqual(wal.distance, 50)

    def test_run(self):

        rn = runner.Runner(name='rn')
        for _ in range(10):
            rn.run()
        self.assertEqual(rn.distance, 100)

    def test_challenge(self):

        wal = runner.Runner(name='wal')
        rn = runner.Runner(name='rn')
        for _ in range(10):
            rn.run()
            wal.walk()
        self.assertNotEqual(rn.distance, wal.distance)

if __name__ == '__main__':
    unittest.main()

