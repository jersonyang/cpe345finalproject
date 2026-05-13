import org.omnetpp.queueing.PassiveQueue;
import org.omnetpp.queueing.Source;
import org.omnetpp.queueing.Sink;
import org.omnetpp.queueing.Server;

network MMC_network
{
    parameters:
        int numServers = default(2);
    submodules:
        gen: Source {
            @display("p=50,150");
        }
        queue: PassiveQueue {
            @display("p=150,150");
        }
        server[numServers]: Server {
            @display("p=250,150");
        }
        sink: Sink {
            @display("p=350,150");
        }
    connections:
        gen.out --> queue.in++;
        for i=0..numServers-1 {
            queue.out++ --> server[i].in++;
            server[i].out --> sink.in++;
        }
}