import java.util.Hashtable;

public class Warhouse implements IOrder {
    String name;
    public Hashtable<String, Integer> stock;

    Warhouse(String name){
        this.name = name;
        this.stock = new Hashtable<String, Integer>();
    }

    void addItem(Item item){
        int x=0;
        if(stock.containsKey(item.name)){
            x = stock.get(item.name).intValue();
        }
        stock.put(item.name, x+item.number);
    }

    @Override
    public void fullfilorder(Order order) {
        for(Item item: order.itemList){
            stock.replace(item.name, stock.get(item.name)-item.number);
        }
        System.out.println("Order fulfiled from "+name);
    }

    public int currentInventory(Item item){
        if(stock.containsKey(item.name)){
            return stock.get(item.name).intValue();
        }
        else
            return -1;
    }

}