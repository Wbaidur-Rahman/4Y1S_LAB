public abstract class Housing {
    String name;

    public void enter(){
        System.out.println("You have entered "+this.name);
    }
    public void exit(){
        System.out.println("Exited from "+this.name);
    }
    public void location(){
        System.out.println("You are in "+this.name);
    }
}
