public class BronzeMember extends Member {

    // Member properties specific to BronzeMember
    private double gasPurchases; // The amount that the member spent on gas in the year.
    private double groceryPurchases; // The amount that the member spent on groceries in the year.
    private double everydayPurchases; // The amount that the member spent on everyday purchases in the year.

    // Constructor for BronzeMember
    public BronzeMember(String name, int age, int yearsMember, String phone, boolean goodStanding,
                        int memberID, int monthJoined, int yearJoined, double dues,
                        double gasPurchases, double groceryPurchases, double everydayPurchases) throws BadMember {

        // Call the superclass (Member) constructor
        super(name, age, yearsMember, phone, goodStanding, memberID, monthJoined, yearJoined, dues);

        // Set properties specific to BronzeMember
        setGasPurchases(gasPurchases);
        setGroceryPurchases(groceryPurchases);
        setEverydayPurchases(everydayPurchases);
    }

    // Getter and Setter methods for BronzeMember-specific properties
    public double getGasPurchases() {
        return this.gasPurchases;
    }

    public void setGasPurchases(double gasPurchases) {
        this.gasPurchases = gasPurchases;
    }

    public double getGroceryPurchases() {
        return this.groceryPurchases;
    }

    public void setGroceryPurchases(double groceryPurchases) {
        this.groceryPurchases = groceryPurchases;
    }

    public double getEverydayPurchases() {
        return this.everydayPurchases;
    }

    public void setEverydayPurchases(double everydayPurchases) {
        this.everydayPurchases = everydayPurchases;
    }

    // Static property for Bronze membership price
    static double Bronzeprice = 50;

    // Implementation of the abstract method to calculate cashback for BronzeMember
    double calculateCashBack() {
        double total = (getGasPurchases() * 0.02) + (getGroceryPurchases() * 0.01) + (getEverydayPurchases() * 0.05);
        return total;
    }

    // Implementation of the abstract method to calculate dues for BronzeMember
    double calculateDues() {
        if (!isGoodStanding()) {
            return Bronzeprice;
        } else {
            return 0;
        }
    }
}
