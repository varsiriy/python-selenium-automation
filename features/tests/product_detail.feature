# Created by varsi at 8/22/2023
Feature: Test for product page

  
  Scenario: User can select colors
    Given Open Amazon product B081YS2F7N page
    Then Verify user can click through colors
    
    
  Scenario: User can select colors
    Given Open Amazon product B07BJKRR25 page
    Then Verify user can select through colors
    
    
  Scenario: User can see deals
    Given Open Amazon Fashion product page
    When Hover over New Arrivals
    Then Verify that user can see the deals