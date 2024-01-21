public abstract class Decorator implements Page{
    Page page;
    Decorator(Page page){
        this.page = page;
    }
    @Override
    public void display() {
        this.page.display();
    }
    
}
