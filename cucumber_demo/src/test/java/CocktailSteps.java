import org.junit.Assert;

import cucumber.api.PendingException;
import cucumber.api.java.en.And;
import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;

public class CocktailSteps {

    private Order order;

    @Given("{string} who wants to buy a drink")
    public void owner_who_wants_to_buy_a_drink(String owner) {
        order = new Order();
        order.declareOwner(owner);
    }

    @When("an order is declared for {string}")
    public void an_order_is_declared_for_target(String target) {
        order.declareTarget(target);
    }

    @And("a message saying {string} is added")
    public void a_message_saying_is_added(String message) {
        order.setMessage(message);
    }

    @Then("there are {string} cocktails in the order")
    public void there_are_cocktails_in_the_order(String string) {
        int nbcocktails = Integer.parseInt(string);
        for (int i = 0; i < nbcocktails; i++) {
            order.addCocktail("cocktail" + i);
        }
        Assert.assertEquals(nbcocktails, order.getCocktails().size());
}

    @Then("the ticket must say {string}")
    public void the_ticket_must_say(String expected) {
        Assert.assertEquals(expected, order.toString());
    }

}
