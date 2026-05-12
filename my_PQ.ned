import org.omnetpp.queueing.Source;
import org.omnetpp.queueing.PassiveQueue;
import org.omnetpp.queueing.Server;
import org.omnetpp.queueing.Sink;
import org.omnetpp.queueing.Classifier;

network my_PQ
{
    submodules:
        source: Source { // High Priority Source
            @display("p=50,100");
        }
        source1: Source { // Low Priority Source
            @display("p=50,200");
        }
        classifier: Classifier { // Sorts the priority
            @display("p=150,150");
        }
        passiveQueue: PassiveQueue { // High Priority Line
            @display("p=250,100");
        }
        passiveQueue1: PassiveQueue { // Low Priority Line
            @display("p=250,200");
        }
        server: Server { // The Rollercoaster
            @display("p=350,150");
        }
        sink: Sink { // The Exit (Where we collect stats)
            @display("p=450,150");
        }
    connections:
        source.out --> classifier.in++;
        source1.out --> classifier.in++;

        // Gate 0 routes Type 0 (High Priority) to the first queue
        classifier.out++ --> passiveQueue.in++;

        // The 'rest' gate catches the Low Priority people
        classifier.rest --> passiveQueue1.in++;

        passiveQueue.out++ --> server.in++;
        passiveQueue1.out++ --> server.in++;
        server.out --> sink.in++;
}