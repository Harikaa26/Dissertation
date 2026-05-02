import csv
import asyncio
import pyshark

# fix Python 3.14 event loop issue
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

TSHARK_PATH = r"C:\Program Files\Wireshark\tshark"

files = [
    ("Scan_Attack.pcapng", 1),
    ("Bruteforce_Simulation.pcapng", 1),
]

output_file = "traffic_dataset.csv"

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow([
        "time",
        "src_ip",
        "dst_ip",
        "protocol",
        "length",
        "src_port",
        "dst_port",
        "label"
    ])

    for file_name, label in files:
        cap = pyshark.FileCapture(
            file_name,
            tshark_path=TSHARK_PATH,
            keep_packets=False
        )

        for pkt in cap:
            try:
                time = pkt.sniff_timestamp
                src_ip = pkt.ip.src if hasattr(pkt, "ip") else ""
                dst_ip = pkt.ip.dst if hasattr(pkt, "ip") else ""
                protocol = pkt.highest_layer
                length = pkt.length
                src_port = pkt[pkt.transport_layer].srcport if hasattr(pkt, "transport_layer") and pkt.transport_layer else ""
                dst_port = pkt[pkt.transport_layer].dstport if hasattr(pkt, "transport_layer") and pkt.transport_layer else ""

                writer.writerow([time, src_ip, dst_ip, protocol, length, src_port, dst_port, label])

            except Exception:
                continue

        cap.close()

print("Dataset created: traffic_dataset.csv")
