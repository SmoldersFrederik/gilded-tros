# -*- coding: utf-8 -*-

class GildedTros(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # Item is no legendary item
            if item.quality != 80:
                # Item are backstage passes for very interesting conferences
                if item.name in [
                    'Backstage passes for Re:Factor',
                    'Backstage passes for HAXX'
                ]:
                    # Increase quality by 1 if sell_in > 10
                    # Increase quality by 2 if 10 >= sell_in > 5
                    # Increase quality by 3 if 5 >= sell_in > 0
                    # Set quality to 0 if sell_in <= 0
                    item.quality += 1 if item.sell_in > 10 else 2 \
                        if item.sell_in > 5 else 3 \
                        if item.sell_in > 0 else -item.quality
                # Item is 'Good Wine'
                elif item.name == 'Good Wine':
                    # Increase quality by 1 if sell_in > 0
                    # Increase quality by 2 if sell_in <= 0
                    item.quality += 1 if item.sell_in > 0 else 2
                # Other items
                else:
                    # Decrease quality by 1 if sell_in > 0
                    # Decrease quality by 2 if sell_in <= 0
                    item.quality -= 1 if item.sell_in > 0 else 2
                # Quality cannot be larger then 50
                if item.quality > 50:
                    item.quality = 50
                # Quality cannot be smaller then 0
                elif item.quality < 0:
                    item.quality = 0
                # Decrease sell_in by 1
                item.sell_in -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
