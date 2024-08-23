public class App {
    public static void main(String[] args) throws Exception {
        EventManager manager=new EventManager();
        
        IEventObserver emailGoogle=new EmailNotifier();
        IEventObserver emailYahoo=new EmailNotifier();
        IEventObserver pushRSS=new PushNotifier();
        IEventObserver fax=new FaxNotifier();

        manager.registerObserver(emailGoogle);
        manager.registerObserver(emailYahoo);
        manager.registerObserver(pushRSS);
        manager.registerObserver(fax);

        manager.notificar("Mensagem Importante!!");
    }
}
