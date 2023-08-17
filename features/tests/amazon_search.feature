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




