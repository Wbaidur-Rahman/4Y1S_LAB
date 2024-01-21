public class Main {
    public static void main(String[] args) {
        Warhouse warhouse = new Warhouse("myWarhouse");
        // ArrayList <Item> items = new ArrayList<Item>();
        Item item;
        for(int i=0;i<100;i++){
            item = new Item(Integer.toString(i), 10+i);
            warhouse.addItem(item);
        }

        OrderFulfilment orderFulfilment = new OrderFulfilment();
        orderFulfilment.addWarhouse(warhouse);

        Order order = new Order(0);

        for(int i=0;i<10;i++){
            item = new Item(Integer.toString(i), 10);
            order.addItem(item);
        }

        orderFulfilment.fullfilorder(order);

    }
}
