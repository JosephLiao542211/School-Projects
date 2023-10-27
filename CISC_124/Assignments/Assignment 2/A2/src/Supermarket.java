public class Supermarket extends Busisness {
    // Private fields for loyalty users, list of departments, and number of products
    private double loyaltyUsers;
    private String[] lisDepartments;
    private int numProducts;

    // Constructor with method header, inherits from the Busisness class
    public Supermarket(int registrationNumber, FranchiseOwner owner, int year, double dailySales, double annualSales, int numProducts, double loyaltyUsers, String[] lisDepartments) throws IllegalBusiness {
        // Call the constructor of the parent class (Busisness) using the "super" keyword
        super(registrationNumber, owner, year, dailySales, annualSales);
        
        // Set the number of products, list of departments, and loyalty users using their respective setter methods
        setNumProducts(numProducts);
        setLisDepartments(lisDepartments);
        setLoyaltyUsers(loyaltyUsers);
    }

    // Getter method to retrieve the number of products
    public int getNumProducts() {
        return numProducts;
    }

    // Setter method to set the number of products
    public void setNumProducts(int numProducts) {
        this.numProducts = numProducts;
    }

    // Getter method to retrieve the number of loyalty users
    public double getLoyaltyUsers() {
        return loyaltyUsers;
    }

    // Setter method to set the number of loyalty users
    public void setLoyaltyUsers(double loyaltyUsers) {
        this.loyaltyUsers = loyaltyUsers;
    }

    // Getter method to retrieve the list of departments
    public String[] getLisDepartments() {
        return lisDepartments;
    }

    // Setter method to set the list of departments
    public void setLisDepartments(String[] lisDepartments) {
        this.lisDepartments = lisDepartments;
    }

    // Override the toString method to provide a custom string representation of the Supermarket object
    @Override
    public String toString() {
        return "Supermarket{" +
               "registrationNumber=" + getRegistrationNumber() +
               ", owner=" + getOwner().getName() +
               ", year=" + getYear() +
               ", dailySales=" + getDailySales() +
               ", annualSales=" + getAnnualSales() +
               ", numProducts=" + numProducts +
               ", loyaltyUsers=" + loyaltyUsers +
               ", lisDepartments=" + String.join(", ", lisDepartments) +
               '}';
    }
}
