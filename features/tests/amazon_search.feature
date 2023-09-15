# Created by varsi at 8/8/2023
Feature: Tests for amazon search
  # Enter feature description here

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for a table
    Then Verify search results is "table"

#  Scenario: Verify that a user can search for a cup
#    Given Open Amazon page
#    When Search for a cup
#    Then Verify search results is "cup"
#
#  Scenario: Verify that a user can search for a dress
#    Given Open Amazon page
#    When Search for a dress
#    Then Verify search results is "dress"

  Scenario Outline: Verify that a user can search for a product
    Given Open Amazon page
    When Search for a <search_word>
    Then Verify search results is <search_result>
    Examples:
    |search_word      |search_result    |
    |cup              |"cup"            |
    |dress            |"dress"          |
    |tea              |"tea"            |
    |coffee           |"coffee"         |
    |forks            |"forks"          |


  Scenario: Verify that user can add item to the cart
    Given Open Amazon page
    When Search for a pen
    When Click on the fist product
    When Store product name
#    When Click One-time purchase radio btn
    When Click Add to Cart btn
    Then Verify the product is Added to Cart
    When Open cart page
    Then Verify cart has 1 item(s)
    Then Verify cart has correct product


  Scenario: Verify that user can see product names and images
    Given Open Amazon page
    When Search for a coffee
    Then Verify that every product has a name and an image


