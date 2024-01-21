public class BasicWebPage implements Webpage {

    public String html = "...";
    public String styleSheet = "...";
    public String script = "...";

    @Override
    public void display() {
        System.out.println("Basic web page!");
    }
}
