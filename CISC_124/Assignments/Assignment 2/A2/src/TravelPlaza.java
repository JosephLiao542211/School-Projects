import java.util.Arrays;

// TravelPlaza class, which extends the Busisness class
public class TravelPlaza extends Busisness {

    // Private fields for dining options, shopping options, and fuel availability
    private String[] diningOptions;
    private String[] shoppingOptions;
    private boolean hasFuel;

    // Constructor with method header, inherits from the Busisness class
    public TravelPlaza(int regNumber, FranchiseOwner owner, int estYear, double dailySales, double annualSales, String[] diningOptions, String[] shoppingOptions, boolean hasFuel) throws IllegalBusiness {
        super(regNumber, owner, estYear, dailySales, annualSales);
        setDiningOptions(diningOptions);
        setShoppingOptions(shoppingOptions);
        this.hasFuel = hasFuel;
    }

    // Getter method to retrieve the dining options
    public String[] getDiningOptions() {
        return diningOptions;
    }

    // Setter method to set the dining options
    public void setDiningOptions(String[] newDiningOptions) {
        this.diningOptions = newDiningOptions;
    }

    // Getter method to retrieve the shopping options
    public String[] getShoppingOptions() {
        return shoppingOptions;
    }

    // Setter method to set the shopping options
    public void setShoppingOptions(String[] newShoppingOptions) {
        this.shoppingOptions = newShoppingOptions;
    }

    // Getter method to check if the plaza has fuel
    public boolean hasFuel() {
        return hasFuel;
    }

    // Setter method to set the fuel availability
    public void setFuel(boolean hasFuel) {
        this.hasFuel = hasFuel;
    }

    // Override the toString method to provide a custom string representation of the TravelPlaza object
    @Override
    public String toString() {
        return "TravelPlaza{" +
                "registrationNumber=" + getRegistrationNumber() +
                ", owner=" + getOwner().getName() +
                ", year=" + getYear() +
                ", dailySales=" + getDailySales() +
                ", annualSales=" + getAnnualSales() +
                ", diningOptions=" + Arrays.toString(diningOptions) +
                ", shoppingOptions=" + Arrays.toString(shoppingOptions) +
                ", fuel=" + (hasFuel ? "Yes" : "No") +
                '}';
    }
}
