Feature: Contact & Professional Links
  As a prospective employer or collaborator
  I want to reach out to Oyendri Sana
  So that I can connect via Email, LinkedIn, or GitHub

  Scenario: Verify external contact channels
    Given the user opens the portfolio homepage
    When the user scrolls to the "Get In Touch" section
    Then the email button should link to Gmail compose for "oyendri.sana.in@gmail.com"
    And the LinkedIn button should link to "https://linkedin.com/in/oyendri-sana-14b73035a"
    And the GitHub button should link to "https://github.com/oyendrisana"
    And all social links should open in a new tab

