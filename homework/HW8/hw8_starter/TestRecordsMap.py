import unittest
from RecordsMap import LocalRecord, RecordsMap

class TestLocalRecord(unittest.TestCase):
    def test_init(self):
        """Test LocalRecord initialization with default rounding and default min/max."""
        record = LocalRecord((12.3456, 78.9012))
        self.assertEqual(record.pos, (12.0, 79.0))
        self.assertIsNone(record.max)
        self.assertIsNone(record.min)

    def test_hash(self):
        """Test hash function consistency based on position."""
        record1 = LocalRecord((10.1234, 20.5678))
        record2 = LocalRecord((10.1234, 20.5678))
        self.assertEqual(hash(record1), hash(record2))

    def test_eq(self):
        """Test equality of LocalRecord instances with same rounded position."""
        record1 = LocalRecord((10.0, 20.0))
        record2 = LocalRecord((10.0, 20.0))
        record3 = LocalRecord((11.0, 21.0))
        self.assertEqual(record1, record2)
        self.assertNotEqual(record1, record3)

    def test_add_report(self):
        """Test that add_report correctly updates min and max temperatures."""
        record = LocalRecord((0, 0))
        record.add_report(30)
        self.assertEqual(record.max, 30)
        self.assertEqual(record.min, 30)

        record.add_report(25)
        self.assertEqual(record.min, 25)
        self.assertEqual(record.max, 30)

        record.add_report(35)
        self.assertEqual(record.max, 35)
        self.assertEqual(record.min, 25)


class TestRecordsMap(unittest.TestCase):
    def test_add_one_report(self):
        """Test adding one report to RecordsMap and check length, retrieval, and containment."""
        rmap = RecordsMap()
        rmap.add_report((5.4, 6.6), 40)

        self.assertEqual(len(rmap), 1)
        self.assertIn((5.4, 6.6), rmap)
        self.assertEqual(rmap[(5.4, 6.6)], (40, 40))

    def test_add_many_reports(self):
        """Test adding multiple reports at multiple locations and check their stored min/max values."""
        rmap = RecordsMap()
        points = [((1.1, 2.2), 30), ((1.1, 2.2), 35), ((9.9, 8.8), 25), ((9.9, 8.8), 20)]

        for pos, temp in points:
            rmap.add_report(pos, temp)

        self.assertEqual(len(rmap), 2)
        self.assertIn((1.1, 2.2), rmap)
        self.assertIn((9.9, 8.8), rmap)
        self.assertEqual(rmap[(1.1, 2.2)], (30, 35))
        self.assertEqual(rmap[(9.9, 8.8)], (20, 25))

        for i in range(10):
            rmap.add_report((i, i), i + 10)
        self.assertGreaterEqual(len(rmap), 10)


if __name__ == '__main__':
    unittest.main()