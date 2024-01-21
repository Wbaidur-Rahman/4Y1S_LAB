import java.util.ArrayList;

public class Order {
    ArrayList <Item> itemList;
    int orderId;
    Order(int orderId){
        itemList = new ArrayList<Item>();
        this.orderId = orderId;
    }

    public int addItem(Item item){
        itemList.add(item);
        return itemList.size()-1;
    }
}
