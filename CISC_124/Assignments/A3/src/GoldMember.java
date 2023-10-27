public class GoldMember extends Member {

    // Member properties specific to GoldMember
    private double restaurantPurchases; // The amount that the member spent at restaurants in the year.
    private double travelPurchases; // The amount that the member spent on travel in the year.

    // Constructor for GoldMember
    public GoldMember(String name, int age, int yearsMember, String phone, boolean goodStanding,
                      int memberID, int monthJoined, int yearJoined, double dues,
                      double restaurantPurchases, double travelPurchases) throws BadMember {

        // Call the superclass (Member) constructor
        super(name, age, yearsMember, phone, goodStanding, memberID, monthJoined, yearJoined, dues);

        // Set properties specific to GoldMember
        this.restaurantPurchases = restaurantPurchases;
        this.travelPurchases = travelPurchases;
    }

    // Getter and Setter methods for GoldMember-specific properties
    public double getRestaurantPurchases() {
        return this.restaurantPurchases;
    }

    public void setRestaurantPurchases(double restaurantPurchases) {
        this.restaurantPurchases = restaurantPurchases;
    }

    public double getTravelPurchases() {
        return this.travelPurchases;
    }

    public void setTravelPurchases(double travelPurchases) {
        this.travelPurchases = travelPurchases;
    }

    // Static property for Gold membership price
    static double Goldprice = 100;

    // Implementation of the abstract method to calculate cashback for GoldMember
    double calculateCashBack() {
        double total = (restaurantPurchases * 0.02) + (travelPurchases * 0.05);
        return total;
    }

    // Implementation of the abstract method to calculate dues for GoldMember
    double calculateDues() {
        if (!isGoodStanding()) {
            return Goldprice;
        } else {
            return 0;
        }
    }
}
