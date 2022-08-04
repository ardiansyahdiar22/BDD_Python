Feature: Booking train ticket on tiket.com

    Feature Description

    Scenario: As a user, i can booking train ticket
        Given Open url tiket.com
        When User choose hometown and destination and user chooses how many passengers
        When User click button search ticket
        Then User can see list available trains