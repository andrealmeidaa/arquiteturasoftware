public class EmailNotifier implements IEventObserver {      
    @Override
    public void update(String msg) {
      System.out.println("Notificação por e-mail: "+msg);  
    }

}
