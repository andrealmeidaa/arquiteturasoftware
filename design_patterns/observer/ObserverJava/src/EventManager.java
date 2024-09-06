import java.util.List;
import java.util.ArrayList;
public class EventManager {
    private List<IEventObserver> observadores;

    public EventManager(){
        this.observadores=new ArrayList<IEventObserver>();
    }

    public void registerObserver(IEventObserver observer){
        this.observadores.add(observer);
    }

    public void notificar(String msg){
        for (IEventObserver observer : this.observadores){
            observer.update(msg);
        }
    }
}
