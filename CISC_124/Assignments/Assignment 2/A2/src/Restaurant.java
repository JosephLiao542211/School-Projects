public class Restaurant extends Busisness {
    // Private fields for drive-thru, mobile ordering, list of meals, rating, and number of seats
    private boolean driveThru;
    private boolean mobileOrdering;
    private String[] lisMeals;
    private int rating;
    private int numSeats;
    

    // Constructor with method header, inherits from the Busisness class
    public Restaurant(int registrationNumber, FranchiseOwner owner, int year, 
                      double dailySales, double annualSales, boolean driveThru, 
                      boolean mobileOrdering, String[] lisMeals, int rating, int numSeats) throws IllegalBusiness {
        // Call the constructor of the parent class (Busisness) using the "super" keyword
        super(registrationNumber, owner, year, dailySales, annualSales);

        // Set the drive-thru, mobile ordering, list of meals, rating, and number of seats using their respective setter methods
        setDriveThru(driveThru);
        setMobileOrdering(mobileOrdering);
        setLisMeals(lisMeals);
        setRating(rating);
        setNumSeats(numSeats);
    }

    // Getter method to check if the restaurant has a drive-thru
    public boolean isDriveThru() {
        return driveThru;
    }

    // Setter method to set whether the restaurant has a drive-thru or not
    public void setDriveThru(boolean newDriveThru) {
        this.driveThru = newDriveThru;
    }

    // Getter method to check if the restaurant has mobile ordering
    public boolean isMobileOrdering() {
        return mobileOrdering;
    }

    // Setter method to set whether the restaurant has mobile ordering or not
    public void setMobileOrdering(boolean newMobileOrdering) {
        this.mobileOrdering = newMobileOrdering;
    }

    // Getter method to retrieve the list of meals offered by the restaurant
    public String[] getLisMeals() {
        return lisMeals;
    }

    // Setter method to set the list of meals offered by the restaurant
    public void setLisMeals(String[] newLisMeals) {
        this.lisMeals = newLisMeals;
    }

    // Getter method to retrieve the rating of the restaurant
    public int getRating() {
        return rating;
    }

    // Setter method to set the rating of the restaurant, with exception handling for invalid ratings
    public void setRating(int newRating) throws IllegalBusiness {
        if (newRating < 1 || newRating > 5) {
            throw new IllegalBusiness("Ratings must be between 1-5.");
        }
        this.rating = newRating;
    }

    // Getter method to retrieve the number of seats in the restaurant
    public int getNumSeats() {
        return numSeats;
    }

    // Setter method to set the number of seats in the restaurant, with exception handling for invalid seat numbers
    public void setNumSeats(int newNumSeats) throws IllegalBusiness {
        if (newNumSeats < 1) {
            throw new IllegalBusiness("Number of seats must be more than 0.");
        }
        this.numSeats = newNumSeats;
    }

    // Override the toString method to provide a custom string representation of the Restaurant object
    @Override
    public String toString() {
        return "Restaurant{" +
                "registrationNumber=" + getRegistrationNumber() +
                ", owner=" + getOwner().getName() +
                ", year=" + getYear() +
                ", dailySales=" + getDailySales() +
                ", annualSales=" + getAnnualSales() +
                ", driveThru=" + driveThru +
                ", mobileOrdering=" + mobileOrdering +
                ", lisMeals=" + String.join(", ", lisMeals) +
                ", rating=" + rating +
                ", numSeats=" + numSeats +
                '}';
    }
}
