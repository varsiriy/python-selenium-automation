# Created by varsi at 8/16/2023
Feature: BestSellers page
  # Enter feature description here

  Scenario: Verify that BestSellers page has correct amount of links
    Given Open BestSellers page
    Then Verify lower header has 5 links