

public class PlatMember extends Member{

   private double entertainmentPurchases; //the amount the member has spent on entertainment in the year.

    private double recurringPurchases; //the amount the member has spent on recurring purchases in the year.

    private double transportationPurchases;// the amount the member has spent on transportation in the year.
    
    static double Platprice=150;

    public PlatMember(String name, int age, int yearsMember, String phone, boolean goodStanding, int memberID, int monthJoined, int yearJoined, double dues, double entertainmentPurchases, double recurringPurchases, double transportationPurchases) throws BadMember {
        
        super(name, age, yearsMember, phone, goodStanding, memberID, monthJoined, yearJoined, dues);
        setEntertainmentPurchases(entertainmentPurchases);
        setRecurringPurchases(recurringPurchases);
        setTransportationPurchases(transportationPurchases);
    }


    public double getEntertainmentPurchases() {
        return entertainmentPurchases;
    }

    public void setEntertainmentPurchases(double entertainmentPurchases) {
        this.entertainmentPurchases = entertainmentPurchases;
    }

    // Getter and Setter for recurringPurchases
    public double getRecurringPurchases() {
        return recurringPurchases;
    }

    public void setRecurringPurchases(double recurringPurchases) {
        this.recurringPurchases = recurringPurchases;
    }

    // Getter and Setter for transportationPurchases
    public double getTransportationPurchases() {
        return transportationPurchases;
    }

    public void setTransportationPurchases(double transportationPurchases) {
        this.transportationPurchases = transportationPurchases;
    }

    // Getter for Platprice (no setter needed as it's a static constant)
  

  
    double calculateCashBack() {
       
        double total=(getEntertainmentPurchases()*0.02)+(getRecurringPurchases()*0.01)+(getTransportationPurchases()*0.05);
        return total;
        
    }


    double calculateDues() {

        if (getGoodStanding() == false){
            if (getYearJoined()>=10)
                return (Platprice-Platprice*0.2);
            else
                return Platprice;
        }
        else
            return 0;
    }

    

         
}