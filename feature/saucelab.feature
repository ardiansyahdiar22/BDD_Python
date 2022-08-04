Feature: Login saucelabs

    Feature Description

    Scenario Outline: As a user i can login to saucelabs, with not valid username valid password, valid username, not valid password, wrong password and username and valid username and password
    	Given Open the url saucelabs
        When Type "<username>" on textfield username
        When Type "<password>" on textfield password
        When Click button login
        Then If login with valid username and password user successfully login, and if login with not valid email and username user can see error message

        Examples:
            | username      | password | 
            | diar          | secret_sauce  | 
            | standard_user | 12121 |
            | diar          | 12122 |
            | standard_user | secret_sauce |


