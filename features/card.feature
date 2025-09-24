Feature: Remove goods/ Change quantities/ Continue Shopping/ Checkout from the shopping cart page

  	Scenario Outline: Add 2 goods to cart
		Given the user is logged in
		When the user click "Add to cart" on "<goods>"
        And the user click on Shopping cart icon
        Then the basket contains "<number>" item on shopping cart page
        And the "<goods>" are present in the shopping cart
		
		Examples:
			| goods                                        | new_status | number |
			| Sauce Labs Bolt T-Shirt, Sauce Labs Backpack | Remove     | 2      |


  	Scenario Outline: User continue shopping from shopping cart page
		Given the user is logged in
		When the user click "Add to cart" on "<goods>"
        And the user click on Shopping cart icon
        And the user click "Continue Shopping" from shopping cart page
        Then the basket contains "<number>" item on shopping cart page
        And the "<goods>" changed status to "<new_status>"
		
		Examples:
			| goods                                        | new_status | number |
			| Sauce Labs Bolt T-Shirt, Sauce Labs Backpack | Remove     | 2      |
    
    @main
  	Scenario Outline: Remove goods from shopping cart page
        Given the user is logged in
        When the user click "Add to cart" on "<added_goods>"
        And the user click on Shopping cart icon
        And the user click "Remove" on "<removed_goods>" from shopping cart page
        Then the basket contains "<number>" item on shopping cart page
        And the "<removed_goods>" is removed from the shopping cart
        And the "<viewed_goods>" is added in the shopping cart
 
    		Examples:
			| added_goods                                  | removed_goods           | viewed_goods        | new_status | number |
			| Sauce Labs Bolt T-Shirt, Sauce Labs Backpack | Sauce Labs Bolt T-Shirt | Sauce Labs Backpack | Remove     | 1      |