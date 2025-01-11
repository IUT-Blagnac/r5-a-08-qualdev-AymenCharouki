Feature: Cocktail Ordering

      As Romeo, I want to offer a drink to Juliette so that we can discuss together.

      Scenario Outline: Creating an empty order
        Given "<owner>" who wants to buy a drink
        When an order is declared for "<target>"
        Then there are "<nbcocktails>" cocktails in the order

        Examples:
          | owner  | target       | nbcocktails |
          | Romeo | Juliette |           0 |
          | Tom   | Jerry    |           0 |

      Scenario Outline: Sending a message with an order
        Given "<owner>" who wants to buy a drink
        When an order is declared for "<target>" 
        And a message saying "<message>" is added
        Then the ticket must say "<expected>"

        Examples:
          | owner  | target       | message     | expected                            |
          | Romeo | Juliette | Wanna chat? | From Romeo to Juliette: Wanna chat? |
          | Tom   | Jerry    | Hei!        | From Tom to Jerry: Hei!             |