public class FaxNotifier implements IEventObserver{
    @Override
    public void update(String msg) {
        System.out.println("Notificação por fax: "+msg);
    }

}
