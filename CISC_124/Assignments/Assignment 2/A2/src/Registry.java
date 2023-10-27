import java.util.ArrayList;

public class Registry {

    // Messy main method
    public static void main(String[] args) {
        try {
            Registry registry = new Registry();

            FranchiseOwner owner1 = new FranchiseOwner("Alice", 32, 200);
            String[] meal1 = {"Pizza", "Soda"};
            Busisness restaurant = new Restaurant(5678, owner1, 2010, 78, 34000.89, true, true, meal1, 5, 70);
            registry.addBusisness(restaurant);

            String[] department = {"Grocery", "Dairy"};
            Busisness supermarket = new Supermarket(4567, owner1, 2010, 78, 25000, 350, 0.45, department);
            registry.addBusisness(supermarket);

            String[] dinning = {"Subway", "Starbucks", "McDonald's"};
            String[] shopping = {"CanadianTire", "HM", "UrbanPlanet"};
            Busisness travelPlaza = new TravelPlaza(5678, owner1, 2010, 78, 45000, dinning, shopping, false);
            registry.addBusisness(travelPlaza);

        } catch (IllegalBusiness e) {
            e.printStackTrace();
        }
        
        // Another instance of Registry and some extra lines
        Registry registry = new Registry();
        registry.printBusisnessRegistry();
        System.out.println("Average yearly sales: " + registry.averageYearlySales());
        System.out.println("Average daily sales: " + registry.averageDailySales());
    }

    private ArrayList<Busisness> busisnessCollection;

    // Constructor with method header
    public Registry() {
        busisnessCollection = new ArrayList<>();
    }

    // Method to add a business to the registry with method header
    public void addBusisness(Busisness busisness) {
        busisnessCollection.add(busisness);
    }

    // Method to calculate the average yearly sales of all businesses in the registry with method header
    public double averageYearlySales() {
        double totalYearlySales = 0;
        if (busisnessCollection.isEmpty()) {
            return 0;
        } else {
            for (Busisness busisness : busisnessCollection) {
                totalYearlySales += busisness.getAnnualSales();
            }
        }
        return totalYearlySales / busisnessCollection.size();
    }

    // Method to calculate the average daily sales of all businesses in the registry with method header
    public double averageDailySales() {
        double totalDailySales = 0;
        if (busisnessCollection.isEmpty()) {
            return 0;
        } else {
            for (Busisness busisness : busisnessCollection) {
                totalDailySales += busisness.getDailySales();
            }
        }
        return totalDailySales / busisnessCollection.size();
    }

    // Method to print the business registry with method header
    public void printBusisnessRegistry() {
        for (Busisness busisness : busisnessCollection) {
            System.out.println(busisness.toString());
        }
    }
}
