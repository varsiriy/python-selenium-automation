# Created by varsi at 8/14/2023
Feature: Signin tests

  Scenario: Verify that clicking Orders takes to signin page
    Given Open Amazon page
    When Click orders
    Then Verify Sing in page opened
    Then Verify email input field presented