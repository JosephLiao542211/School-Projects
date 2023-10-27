import java.util.ArrayList;

public class OnlineOrder {

    // Member properties
    private Member member; // The member who is placing the order.
    private double costOrder; // The cost of the order.
    private int numItems; // The number of items in the order.
    private ArrayList<GroceryItem> basketItems; // An ArrayList of items in the customer's basket.

    // Constructor for OnlineOrder
    public OnlineOrder(Member member, ArrayList<GroceryItem> basketItems) throws BadOrder {
        this.member = member;
        setBasketItems(basketItems);
        setCostOrder();
        setNumItems();
    }

    // Getter and Setter methods for various properties
    public Member getMember() {
        return this.member;
    }

    public void setMember(Member member) {
        this.member = member;
    }

    public double getCostOrder() {
        return this.costOrder;
    }

    public void setCostOrder() {
        this.costOrder = totalCostBasket(getBasketItems());
    }

    public int getNumItems() {
        return this.numItems;
    }

    public void setNumItems() {
        this.numItems = getBasketItems().size();
    }

    public ArrayList<GroceryItem> getBasketItems() {
        return this.basketItems;
    }

    public void setBasketItems(ArrayList<GroceryItem> basketItems) throws BadOrder {
        // Check if each item in the basket is in stock
        try {
            for (GroceryItem item : basketItems) {
                if (item.getInventory() == 0) {
                    throw new BadOrder("Item '" + item.getItemName() + "' is not in stock.");
                }
            }
        } catch (BadOrder e) {
            System.out.println(getMember().getName() + "'s order has an error: " + e.getMessage());
        }
        
        // If all items are in stock, set the basketItems ArrayList
        this.basketItems = basketItems;
    }

    // Checks if all items in the basket are in stock
    public boolean checkInventory() {
        for (GroceryItem item : basketItems) {
            if (item.getInventory() == 0) {
                return false;
            }
        }
        return true;
    }

    // Calculates the total cost of the order
    public double totalCostBasket(ArrayList<GroceryItem> basket) {
        double total = 0;
        for (GroceryItem item : basketItems) {
            total += item.getPrice();
        }
        return total;
    }

    // Compare two orders based on their total costs
    public String compareTo(OnlineOrder comparedOrder) {
        double x = totalCostBasket(getBasketItems());
        double y = comparedOrder.totalCostBasket(comparedOrder.getBasketItems());

        return ("Order A costs: " + x + " while Order B costs: " + y);
    }

    // toString method to represent the object's state as a string
    @Override
    public String toString() {
        return "{" +
                " member:'" + getMember().getName() + "'" +
                ", costOrder:'" + getCostOrder() + "'" +
                ", numItems:'" + getNumItems()+"}";
    }
}
