public class FranchiseOwner {
    private int age;
    private int businessYears;
    private String name;

    // Constructor with method headers
    public FranchiseOwner(String name, int age, int businessYears) throws IllegalBusiness {
        this.name = name;
        setAge(age); // Set the age using the provided method
        setBusinessYears(businessYears); // Set businessYears using the provided method
    }

    // Getter method to retrieve the owner's name
    public String getName() {
        return name;
    }

    // Setter method to set the owner's name
    public void setName(String name) {
        this.name = name;
    }

    // Getter method to retrieve the owner's age
    public int getAge() {
        return age;
    }

    // Setter method to set the owner's age
    public void setAge(int age) throws IllegalBusiness {
        if (age < 18) {
            throw new IllegalBusiness("Owner must be 18+.");
        }
        this.age = age;
    }

    // Getter method to retrieve the owner's years in business
    public int getBusinessYears() {
        return businessYears;
    }

    // Setter method to set the owner's years in business
    public void setBusinessYears(int businessYears) throws IllegalBusiness {
        if (businessYears > 110) {
            throw new IllegalBusiness("Owner's maximum age is 110.");
        }
        this.businessYears = businessYears;
    }

    // Override the toString method to provide a custom string representation of the object
    @Override
    public String toString() {
        return "FranchiseOwner [Name=" + name 
               + ", Age=" + age 
               + ", Years in Business=" + businessYears + "]";
    }
}
