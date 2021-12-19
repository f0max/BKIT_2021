Feature: Testing the biquadratic equation solution
    Scenario: Test when A = 1; B = -5; C = 6
        Given coefs are 1, -5 and 6
        When counting roots          
        Then the roots are -1.73, 1.73, -1.41 and 1.41