public abstract class Member {

    // Member properties
    private String name; // The name of the membership holder.
    private int age; // The age of the membership holder (a member must be 18 years or older).
    private int yearsMember; // The number of years that the customer has been a member.
    private String phone; // The member's telephone number.
    private boolean goodStanding; // True if the customer's membership is paid.
    private int memberID; // The member's ID.
    private int monthJoined; // The month that the member joined (this value must be between 1 and 12).
    private int yearJoined; // The year that the member joined (this must be greater than or equal to 2013 -- the year the store opened).
    private double dues; // The annual fee for the customer's membership.

    // Constructor
    public Member(String name, int age, int yearsMember, String phone, boolean goodStanding,
                  int memberID, int monthJoined, int yearJoined, double dues) throws BadMember {
        this.name = name;
        setAge(age);
        this.yearsMember = yearsMember;
        this.phone = phone;
        this.goodStanding = goodStanding;
        this.memberID = memberID;
        setMonthJoined(monthJoined);
        setYearJoined(yearJoined);
        this.dues = dues;
    }

    // Getter and Setter methods for various properties
    public String getName() {
        return this.name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return this.age;
    }

    public void setAge(int age) throws BadMember {
        try {
            if (age < 18) {
                throw new BadMember("Must be above 18 to be a member");
            }
        } catch (BadMember e) {
            System.out.println(getName() + " " + e.getMessage());
        } finally {
            this.age = age;
        }
    }

    public int getYearsMember() {
        return this.yearsMember;
    }

    public void setYearsMember(int yearsMember) {
        this.yearsMember = yearsMember;
    }

    public String getPhone() {
        return this.phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public boolean isGoodStanding() {
        return this.goodStanding;
    }

    public boolean getGoodStanding() {
        return this.goodStanding;
    }

    public void setGoodStanding(boolean goodStanding) {
        this.goodStanding = goodStanding;
    }

    public int getMemberID() {
        return this.memberID;
    }

    public void setMemberID(int memberID) {
        this.memberID = memberID;
    }

    public int getMonthJoined() {
        return this.monthJoined;
    }

    public void setMonthJoined(int monthJoined) throws BadMember {
        try {
            if (monthJoined > 12 || monthJoined < 1) {
                throw new BadMember("Month joined must be between 1-12");
            } else {
                this.monthJoined = monthJoined;
            }
        } catch (BadMember e) {
            System.out.println(getName() + " has an error: " + e.getMessage());
        }
    }

    public int getYearJoined() {
        return this.yearJoined;
    }

    public void setYearJoined(int yearJoined) throws BadMember {
        try {
            if (yearJoined < 2013) {
                throw new BadMember("Must be after 2013 (store opening)");
            }
        } catch (BadMember e) {
            System.out.println(getName() + " has an error: " + e.getMessage());
        }
    }

    public double getDues() {
        return this.dues;
    }

    public void setDues(double dues) {
        this.dues = dues;
    }

    // Method to calculate cashback (to be implemented by subclasses)
    abstract double calculateCashBack();

    // Method to calculate dues (to be implemented by subclasses)
    abstract double calculateDues();

    // toString method to represent the object's state as a string
    @Override
    public String toString() {
        return "The member's name is " + getName() + ". They have been a member for " + getYearsMember() + " years.";
    }

    // Method to compare two members based on years of membership
    public String compareTo(Member comparedMember) {
        double x = this.yearsMember;
        double y = comparedMember.getYearsMember();

        return ("Member a has joined for: " + x + " years while member b has joined for: " + y + " years");
    }
}
