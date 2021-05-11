# -*- coding: utf-8 -*-
import unittest

from gilded_tros import Item, GildedTros


class GildedTrosTest(unittest.TestCase):
    def test_foo(self):
        items = [Item('foo', 0, 0)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].name, 'foo')

    def test_negative_quality(self):
        items = [Item('foo', 10, 0)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 0)

    def test_default_item(self):
        items = [
            Item('foo', 1, 10),
            Item('foo', 0, 10),
        ]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 9)
        self.assertEqual(items[1].quality, 8)

    def test_good_wine(self):
        items = [
            Item('Good Wine', 10, 40),
            Item('Good Wine', 0, 40),
            Item('Good Wine', 0, 50),
        ]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 41)
        self.assertEqual(items[1].quality, 42)
        self.assertEqual(items[2].quality, 50)

    def test_legendary_item(self):
        items = [Item('B-DAWG Keychain', 10, 80)]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].sell_in, 10)
        self.assertEqual(items[0].quality, 80)

    def test_backstage_passes(self):
        items = [
            Item('Backstage passes for Re:Factor', 11, 20),
            Item('Backstage passes for Re:Factor', 10, 20),
            Item('Backstage passes for Re:Factor', 5, 20),
            Item('Backstage passes for Re:Factor', 0, 20),
            Item('Backstage passes for Re:Factor', 5, 49),
        ]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 21)
        self.assertEqual(items[1].quality, 22)
        self.assertEqual(items[2].quality, 23)
        self.assertEqual(items[3].quality, 0)
        self.assertEqual(items[4].quality, 50)

    def test_smelly_items(self):
        items = [
            Item('Duplicate Code', 1, 10),
            Item('Duplicate Code', 0, 10),
            Item('Duplicate Code', 1, 1),
        ]
        gilded_tros = GildedTros(items)
        gilded_tros.update_quality()
        self.assertEqual(items[0].quality, 8)
        self.assertEqual(items[1].quality, 6)
        self.assertEqual(items[2].quality, 0)


if __name__ == '__main__':
    unittest.main()
