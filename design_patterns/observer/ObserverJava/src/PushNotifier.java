public class PushNotifier implements IEventObserver {
    @Override
    public void update(String msg) {
        System.out.println("Notificação Push: " + msg);
    }
}
