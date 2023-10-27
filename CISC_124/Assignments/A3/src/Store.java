import java.util.ArrayList;

// The main class representing the store
public class Store {

    // Main method
    public static void main(String[] args) throws BadMember, BadOrder {
        // Create an ArrayList to store member information
        ArrayList<Member> memberDB = new ArrayList<Member>();

        // Create instances of different member types and add them to the member database ALSO TESTS ERROR HANDLEING
        Member memb1 = new GoldMember("Bob Jones", 15, 5, "674-829-2342", true, 6783421, 6, 2018, 556, 234, 122130);
        memberDB.add(memb1);

        Member memb2 = new BronzeMember("Tahani Jane", 56, 10, "896-234-8767", true, 8573623, 6, 2003, 789, 456, 324, 102012);
        memberDB.add(memb2);

        Member memb3 = new PlatMember("Bill Jane", 56, 10, "896-234-8767", true, 8573623, 622, 2013, 789, 456, 324, 102012);
        memberDB.add(memb3);

        // Loop through the member database and print each member's name
        for (int i = 0; i < memberDB.size(); i++) {
            System.out.println(memberDB.get(i).getName());
        }

        // Create ArrayLists to store grocery order items
        ArrayList<GroceryItem> order = new ArrayList<GroceryItem>();
        ArrayList<GroceryItem> orderb = new ArrayList<GroceryItem>();

        // Create instances of GroceryItem and add them to the orders
        GroceryItem item1 = new GroceryItem("Bananas", 1.50, 45, 32114, GroceryCategory.PRODUCE);
        GroceryItem item2 = new GroceryItem("Cat", 122.50, 452, 32434114, GroceryCategory.MEAT);
        GroceryItem item3 = new GroceryItem("Peppers", 12.50, 0, 32434114, GroceryCategory.PRODUCE);
        order.add(item1);
        order.add(item2);
        orderb.add(item3);

        // Create instances of OnlineOrder using members and their respective orders
        OnlineOrder order1 = new OnlineOrder(memb3, order);
        OnlineOrder order2 = new OnlineOrder(memb2, orderb);

        // Print the name of the first item in the first order's basket
        System.out.println((order1.getBasketItems()).get(0).getItemName());

        // Print the name of the member and the items in the second order's basket
        System.out.println(order2.getMember().getName() + "'s Order:");
        for (GroceryItem item : order2.getBasketItems()) {
            System.out.println(item.getItemName());
        }

        // Compare the membership lengths of two members and print the result
        System.out.println(memb3.compareTo(memb2));

        // Compare the total costs of two orders and print the result
        System.out.println(order1.compareTo(order2));

        // Print the toString representation of a member, a grocery item, and an online order
        System.out.println(memb1.toString());
        System.out.println(item1.toString());
        System.out.println("Order summary:"+order1.toString());
    }
}
