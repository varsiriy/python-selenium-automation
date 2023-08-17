# Created by varsi at 8/17/2023
Feature: Add item to the cart


  Scenario: Verify that user can add item to the cart
    Given Open Amazon page
    When Search for a dog food
    Then Click on the fist product
    Then Click One-time purchase radio btn
    Then Click Add to Cart btn
    Then Verify the product is Added to Cart