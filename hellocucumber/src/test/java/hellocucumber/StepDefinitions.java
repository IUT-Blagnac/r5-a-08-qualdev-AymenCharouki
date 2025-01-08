package hellocucumber;

import io.cucumber.java.en.*;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Assertions.*;

public class StepDefinitions {

    private String today = null;
    private String reponse = null;

    @Given("an example scenario")
    public void anExampleScenario() {
    }

    @When("all step definitions are implemented")
    public void allStepDefinitionsAreImplemented() {
    }

    @Then("the scenario passes")
    public void theScenarioPasses() {
    }
    
    @Given("aujourd'hui c'est {string}")
    public void today_is(String day) {
        today = day;
    }
    
    @When("je demande si c'est déjà vendredi")
    public void i_ask_whether_it_s_friday_yet() {
        reponse = isItFriday.isItFriday(today);
    }
   
    @Then("on devrait me dire {string}")
    public void i_should_be_told_friday(String string) {
        assertEquals(reponse, string);
    }
}
