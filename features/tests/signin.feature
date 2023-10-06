@signin
Feature: Signin tests

  Scenario: Verify that clicking Orders takes to signin page
    Given Open Amazon page
    When Click orders
    Then Verify Sign in page opened
  @smoke
  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify Sign in page opened

  Scenario: Amazon users see sign in button
    Given Open Amazon page
    Then Verify Sign In is clickable
    When Wait for 3 sec
    Then Verify Sign In is clickable
    Then Verify Sign In disappears