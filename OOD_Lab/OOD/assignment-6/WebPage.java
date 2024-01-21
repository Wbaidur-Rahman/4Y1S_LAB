public class WebPage implements Page{
    String html = "";
    String css = "";
    String js = "";
    
    @Override
    public void display() {
       System.out.println("Fundamental Webpage");
    }
}
