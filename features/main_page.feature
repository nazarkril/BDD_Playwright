Feature: Added/Remove/Sorting goods from the main page


	@main
	Scenario Outline: Add goods to cart
		Given the user is logged in
		When the user click "Add to cart" on "<goods>"
		Then the basket contains "<number>" item
		And the "<goods>" changed status to "<new_status>"

		Examples:
			| goods                 | old_status   | new_status | number |
			| Sauce Labs Bike Light | Add to cart  | Remove     | 1      |


	@main
  	Scenario Outline: Add 2 goods to cart
		Given the user is logged in
		When the user click "Add to cart" on "<goods>"
		Then the basket contains "<number>" item
		And the "<goods>" changed status to "<new_status>"

		Examples:
			| goods                                        | new_status | number |
			| Sauce Labs Bolt T-Shirt, Sauce Labs Backpack | Remove     | 2      |

  	@main
	Scenario Outline: Remove goods from cart on main page
		Given the user is logged in
		When the user click "Add to cart" on "<goods>"
		And the user click "Remove" on "<goods>" from main page
		Then the basket contains "<number>" item
		And the "<goods>" changed status to "<new_status>"

		Examples:
			| goods                    | old_status   | new_status | number |
			| Sauce Labs Fleece Jacket | Remove       | Add to cart| 0      |


	@main
  	Scenario Outline: Add good after removing it from cart on main page
		Given the user is logged in
		When the user click "Add to cart" on "<goods>"
		And the user click "Remove" on "<goods>" from main page
		And the user click "Add to cart" on "<goods>"
		Then the basket contains "<number>" item
		And the "<goods>" changed status to "<new_status>"

		Examples:
			| goods             | old_status  | new_status | number |
			| Sauce Labs Onesie | Add to cart | Remove     | 1      |

	
	@main
	Scenario Outline: Sorting goods by option
		# This scenario verifies that sorting options correctly reorder the goods list and display the expected first item and price.
		Given the user is logged in
		When the user sorts goods by "<option_text>"
		Then the goods is sorted by "<option_text>"
		And the name of the first item is "<first_item>"
		And the price of the first item is "<price_first_item>"

		Examples:
			| option_text         | first_item                              | price_first_item |
			| Name (A to Z)       | Sauce Labs Backpack                     | $29.99             |
			| Name (Z to A)       | Test.allTheThings() T-Shirt (Red)       | $15.99             |
			| Price (low to high) | Sauce Labs Onesie                       | $7.99              |
			| Price (high to low) | Sauce Labs Fleece Jacket                | $49.99             |