# Created by varsi at 8/16/2023
Feature: Tests for Main page UI
  # Enter feature description here

  Scenario: Verify that footer has correct amount of links
    Given Open Amazon page
    Then Verify footer has 35 links

  Scenario: Verify that footer has many of links
    Given Open Amazon page
    Then Verify many links are shown in the footer