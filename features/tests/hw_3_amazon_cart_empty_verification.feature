# Created by varsi at 8/9/2023
Feature: Test for amazon cart


  Scenario: Verify that Amazon cart is empty after clicking it
    Given Open Amazon page
    When Click on the cart icon
    Then Verify that Amazon cart is empty