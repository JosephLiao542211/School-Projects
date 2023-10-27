public class GroceryItem {

    // Member properties
    private String itemName; // The name of the item.
    private double price; // The price of the item (this value must be greater than $0).
    private int inventory; // How many units of the item are in stock in inventory.
    private int SKU; // The SKU (barcode number) for the item.

    // Constructor for GroceryItem
    public GroceryItem(String itemName, double price, int inventory, int SKU, GroceryCategory category) {
        this.itemName = itemName;
        this.price = price;
        this.inventory = inventory;
        this.SKU = SKU;
    }

    // Getter and Setter methods for various properties
    public String getItemName() {
        return this.itemName;
    }

    public void setItemName(String itemName) {
        this.itemName = itemName;
    }

    public double getPrice() {
        return this.price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getInventory() {
        return this.inventory;
    }

    public void setInventory(int inventory) {
        this.inventory = inventory;
    }

    public int getSKU() {
        return this.SKU;
    }

    public void setSKU(int SKU) {
        this.SKU = SKU;
    }

    // toString method to represent the object's state as a string
    @Override
    public String toString() {
        return getItemName() + " costs: " + getPrice() + "$ and there are " + getInventory() + " in inventory";
    }
}
