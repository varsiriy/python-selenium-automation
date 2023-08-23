# Created by varsi at 8/17/2023
Feature: Add item to the cart


  Scenario: Verify that user can add item to the cart
    Given Open Amazon page
    When Search for a dog food
    When Click on the fist product
    When Store product name
    When Click One-time purchase radio btn
    When Click Add to Cart btn
    Then Verify the product is Added to Cart
    When Open cart page
    Then Verify cart has 1 item(s)
    Then Verify cart has correct product