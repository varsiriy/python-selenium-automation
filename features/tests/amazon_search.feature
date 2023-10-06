Feature: Tests for amazon search

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for a table
    Then Verify search results is "table"

#  Scenario: Verify that a user can search for a cup
#    Given Open Amazon page
#    When Search for a cup
#    Then Verify search results is "cup"
  @smoke
  Scenario: Verify that a user can search for a tea
    Given Open Amazon page
    When Search for tea
    Then Verify search results is "tea"

  Scenario Outline: Verify that a user can search for a product
    Given Open Amazon page
    When Search for <search_word>
    Then Verify search results is <search_result>
    Examples:
    |search_word      |search_result    |
    |cup              |"cup"            |
    |dress            |"dress"          |
    |tea              |"tea"            |
    |coffee           |"coffee"         |
    |forks            |"forks"          |

  @smoke
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
    When Search for coffee
    Then Verify that every product has a name and an image


  Scenario Outline: User can select and search in a department
    Given Open Amazon page
    When Select department by alias <dept_alias>
    And Search for <search_word>
    Then Verify <selected_dept> department is selected
    Examples:
    |dept_alias   |search_word   |selected_dept   |
    |stripbooks   |Faust         |books           |
    |audible      |Alice in      |audible         |


