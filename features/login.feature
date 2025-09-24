Feature: Login/Logout and user sessions

	@main
	Scenario: Successful login
		Given the user is on the SauceDemo login page
		When user1 enter valid credentials
		Then they should be redirected to the inventory page

	@main
	Scenario Outline: User can proceed add goods to cart after re-login
		Given the user is on the SauceDemo login page
		When user1 enter valid credentials
		And the user click "Add to cart" on "<goods>"
		And user log out
		And user2 enter valid credentials
		Then the basket contains "<number>" item
		And the "<goods>" changed status to "<new_status>"

		Examples:
			| goods               | number | new_status |
			| Sauce Labs Backpack | 1      | Remove     |

	@main
	Scenario: Locked out user cannot log in
		Given the user is on the SauceDemo login page
		When user3 enter valid credentials
		Then the error message is "Epic sadface: Sorry, this user has been locked out."

	@main
	Scenario: User1 selected goods User2 cannot see them in the cart
		Given the user is on the SauceDemo login page
		When user1 enter valid credentials
		And the user click "Add to cart" on "Sauce Labs Bike Light"
		And user log out
		And user2 enter valid credentials
		Then the basket contains "0" item
