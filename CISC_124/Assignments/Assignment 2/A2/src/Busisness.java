public class Busisness {
    // Fields to store the registration number, owner, year of establishment, daily sales, and annual sales
    int registrationNumber;
    FranchiseOwner owner;
    int year;
    double dailySales;
    double annualSales;

    // Constructor with method header
    public Busisness(int registrationNumber, FranchiseOwner owner, int year, double dailySales, double annualSales) throws IllegalBusiness {
        // Initialize the fields with the provided values
        this.registrationNumber = registrationNumber;
        this.owner = owner;
        this.year = year;
        setDailySales(dailySales);
        setAnnualSales(annualSales); 
    }

    // Setter method to set the year of establishment
    public void setYear(int year) {
        this.year = year;
    }
    
    // Setter method to set the registration number
    public void setRegistrationNumber(int registrationNumber) {
        this.registrationNumber = registrationNumber;
    }

    // Setter method to set the owner
    public void setOwner(FranchiseOwner owner) {
        this.owner = owner;
    }

    // Getter method to retrieve the registration number
    public int getRegistrationNumber() {
        return registrationNumber;
    }
    
    // Getter method to retrieve the owner
    public FranchiseOwner getOwner() {
        return owner;
    }

    // Getter method to retrieve the year of establishment
    public int getYear() {
        return year;
    }
    
    // Getter method to retrieve the daily sales
    public double getDailySales() {
        return dailySales;
    }

    // Setter method to set the daily sales, with exception handling for negative or zero values
    public void setDailySales(double dailySales) throws IllegalBusiness {
        if (dailySales <= 0) {
            throw new IllegalBusiness("Daily sales must be greater than 0.");
        }
        this.dailySales = dailySales;
    }
    
    // Getter method to retrieve the annual sales
    public double getAnnualSales() {
        return annualSales;
    }

    // Setter method to set the annual sales, with exception handling for negative or zero values
    public void setAnnualSales(double annualSales) throws IllegalBusiness {
        if (annualSales <= 0) {
            throw new IllegalBusiness("Annual sales must be greater than 0.");
        }
        this.annualSales = annualSales;
    }

    // Override the toString method to provide a custom string representation of the Business object
    @Override
    public String toString() {
        return "Business [Registration Number=" + registrationNumber 
               + ", Owner=" + owner.getName() 
               + ", Established Year=" + year 
               + ", Daily Sales=" + dailySales 
               + ", Annual Sales=" + annualSales + "]";
    }
    
}
