import org.omnetpp.queueing.Queue;
import org.omnetpp.queueing.Source;
import org.omnetpp.queueing.Sink;

network Queueing_network
{
    submodules:
        gen: Source {
            @display("p=134,150");
        }
        fifo: Queue {
            @display("p=134,30");
        }
        sink: Sink;
    connections:
        gen.out --> fifo.in++;
        fifo.out --> sink.in++;
}
