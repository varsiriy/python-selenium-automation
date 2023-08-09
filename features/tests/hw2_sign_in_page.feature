# Created by varsi at 8/8/2023
Feature: Test for sign in page. Hw_2
  # Enter feature description here

  Scenario: Verify that logged out user sees Sigh in when clicking on Returns and Orders
    Given Open Amazon page
    When Click orders
    Then Verify Sing in page opened
    Then Verify email input field presented