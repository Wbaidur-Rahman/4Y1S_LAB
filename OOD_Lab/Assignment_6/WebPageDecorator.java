public abstract class WebPageDecorator implements Webpage {
    protected Webpage webpage;

    WebPageDecorator(Webpage webpage) {
        this.webpage = webpage;
    }

    public void display(){
        this.webpage.display();
    }

}
