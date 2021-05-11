# -*- coding: utf-8 -*-
import unittest

from gilded_tros import Item, GildedTros


class GildedTrosTest(unittest.TestCase):
    def test_foo(self):
        items = [Item('foo', 0, 0)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].name, 'foo')

    def test_positive_sell_by_date(self):
        items = [Item('foo', 2, 10)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 9)

    def test_negative_sell_by_date(self):
        items = [Item('foo', 0, 10)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 8)

    def test_negative_quality(self):
        items = [Item('foo', 10, 0)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_good_wine(self):
        items = [Item('Good Wine', 10, 49)]
        gilded_tros = GildedTros(items)
        for i in range(2):
            gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 50)

    def test_legendary_item(self):
        items = [Item('B-DAWG Keychain', 10, 80)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].sell_in, 10)
        self.assertEqual(items[0].quality, 80)

    def test_backstage_passes(self):
        items = [Item('Backstage passes for Re:Factor', 11, 20)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 21)
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 23)
        items[0].sell_in = 5
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 26)
        items[0].sell_in = 0
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 0)



if __name__ == '__main__':
    unittest.main()
