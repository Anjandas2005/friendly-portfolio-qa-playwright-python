Feature: Portfolio Navigation & Routing
  As a visitor to Oyendri Sana's portfolio
  I want to use the navigation bar
  So that I can explore different sections and the CV page

  Scenario: User visits the homepage and views branding
    Given the user opens the portfolio homepage
    Then the navigation bar should display logo "Oyendri Sana"
    And the page title should be "Oyendri Sana | Curriculum Vitae"

  Scenario: User navigates from Home to About page and back
    Given the user opens the portfolio homepage
    When the user clicks on the "About" navigation link
    Then the page title should change to "About Me | Oyendri Sana"
    And the current URL should include "about.html"
    When the user clicks on the "Home" navigation link
    Then the current URL should be the homepage

