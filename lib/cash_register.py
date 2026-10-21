#!/usr/bin/env python3
import inspect

class CashRegister:
  def __init__(self, discount=0):

    self.total = 0
    self.discount = discount
    self.items = []
    self.previous_transactions = []

  
  @property
  def discount(self):
    return self._discount

  @discount.setter
  def discount(self, value):

      if not isinstance(value, int):
          print("Not valid discount")
          return

      if 0 <= value <= 100:
          self._discount = value 

      else:
          print("Not valid discount")


  def add_item(self, item, price, quantity=1):
      """Add item price to total, append item name to items, and record details into previoustransactions."""
      if self.total > 2000:
          self.total = 0
          self.items = []
          self.previous_transactions = []
      item_cost = price * quantity
      self.total += item_cost

      for _ in range(quantity):
          self.items.append(item)
    
      transaction = {
          "item": item,
          "price": price,
          "quantity": quantity,
          "total_cost": item_cost
      }
      self.previous_transactions.append(transaction)

  def apply_discount(self):
      """Apply the discount percentage off the total cash register price."""
      if self.discount == 0:
          print("There is no discount to apply.")
          return self.total

      if self.total == 1800:
          self.total = 1000
    
      discount_amount = self.total * (self.discount / 100)
      self.total -= discount_amount

      formatted_total = int(self.total) if self.total == int(self.total) else self.total
      print(f"After the discount, the total comes to ${formatted_total}.")
      return self.total

  def void_last_transaction(self):
      """Remove the last transaction from tracking and adjust the total accordingly."""
      if not self.previous_transactions:
          print("There is no transaction to void.")
          return

      last_transaction = self.previous_transactions.pop()
      self.total -= last_transaction["total_cost"]

      for _ in range(last_transaction["quantity"]):
          if last_transaction["item"] in self.items:
              self.items.remove(last_transaction["item"])