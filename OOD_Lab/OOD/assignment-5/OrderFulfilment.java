import java.util.ArrayList;

public class OrderFulfilment implements IOrder{
    ArrayList <Warhouse> warhouses;

    OrderFulfilment(){
        warhouses = new ArrayList<Warhouse>();
    }

    int addWarhouse(Warhouse warhouse){
        warhouses.add(warhouse);
        return warhouses.size()-1;
    }

    @Override
    public void fullfilorder(Order order) {
        boolean check = true;
        for(Warhouse warhouse : warhouses ){
            check = true;
            for(Item item: order.itemList)
                if(warhouse.currentInventory(item)<item.number) check = false;
            if(check){
                warhouse.fullfilorder(order);
            }
            else{
                System.out.println("Order cannot be fulfilled");
            }

            for(Item item: order.itemList){
                System.out.println(warhouse.currentInventory(item));
            }
        }
    }
}
