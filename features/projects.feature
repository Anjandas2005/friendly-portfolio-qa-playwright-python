Feature: Featured Projects Showcase
  As a recruiter or collaborator
  I want to inspect Oyendri Sana's featured projects
  So that I can evaluate their development experience

  Scenario: View featured project cards and technologies
    Given the user opens the portfolio homepage
    When the user views the "Featured Projects" section
    Then there should be 3 project cards displayed
    And the projects should include "Netflix Clone", "Energy Bill Optimization", and "Intelligent Health Assistant(in progress)"

