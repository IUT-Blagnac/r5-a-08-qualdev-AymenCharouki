import java.util.ArrayList;
import java.util.List;

public class Order {
    private String owner;
    private String target;
    private String message;
    private List<String> cocktails;

    public Order() {
        this.owner = "";
        this.target = "";
        this.cocktails = new ArrayList<>();
    }

    public String getOwner() {
        return owner;
    }

    public String getTarget() {
        return target;
    }

    public void declareOwner(String owner) {
        this.owner = owner;
    }

    public void declareTarget(String target) {
        this.target = target;
    }

    public void addCocktail(String cocktail)   {
        this.cocktails.add(cocktail);
    }

    public List<String> getCocktails() {
        return cocktails;
    }

    public String getMessage() {
        return message;
    }
    
    public void setMessage(String message) {
        this.message = message;
    }
    @Override
    public String toString() {
        return "From " + owner + " to " + target + ": " + message;
    }

}
