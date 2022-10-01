import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['topbid']['price'], quote['topask']['price'], (quote['topbid']['price'] + quote['topask']['price'])/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['topbid']['price'], quote['topask']['price'], (quote['topbid']['price'] + quote['topask']['price'])/2))


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_calculateRatio(self):
    priceA = ((120.48 + 119.2)/2)
    priceB = ((121.68 + 117.87)/2)

    self.assertEqual(getRatio(priceA, priceB), (priceA/priceB))
  
  def test_getRatio_priceA_isZero(self):
    priceA = 0
    priceB = ((121.68 + 117.87)/2)

    self.assertEqual(getRatio(priceA, priceB), (priceA/priceB))

    def test_getRatio_priceB_isZero(self):
    priceA = ((120.48 + 119.2)/2)
    priceB = 0

    self.assertEqual(getRatio(priceA, priceB), (priceA/priceB))


if __name__ == '__main__':
    unittest.main()
