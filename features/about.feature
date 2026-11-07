Feature: About Me and Academic Credentials
  As an interviewer or visitor
  I want to read Oyendri Sana's academic background and technical skills
  So that I can review qualifications for software development roles

  Scenario: Verify education and technical skills
    Given the user navigates directly to the About page
    Then the main heading should be "About Me"
    And there should be 3 education history items listed
    And the primary degree should be "B.Tech in Computer Science Engineering"
    And the technical skills should include "Programming Languages", "Web & Frontend", and "Core CS Concepts"

