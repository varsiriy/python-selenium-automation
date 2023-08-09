# Created by varsi at 8/8/2023
Feature: Tests for amazon search
  # Enter feature description here

  Scenario: Verify that a user can search for a table
    Given Open Amazon page
    When Search for a table
    Then Verify search results is correct

