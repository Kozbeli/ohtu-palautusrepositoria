*** Settings***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  foo  bar12345
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  asdf  asdf1234
    Output Should Contain  User with username asdf already exists

Register With Too Short Username And Valid Password
    Input Credentials  as  asdf1234
    Output Should Contain  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  hjkl  hjkl1
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    input Credentials  hjkl  hjklhjlk
    Output Should Contain  Password must contain at least one number

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  asdf  asdf12345