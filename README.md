**Hardened LAN Architecture with AI-Assisted Threat Detection Using MITRE ATT&CK**


This repository contains all experimental output files generated as part of the dissertation submitted for the degree of Master's in Computing at the University of East London.

Tools Used:
Python 3, pyshark, pandas, scikit-learn
Wireshark
VMware Workstation Pro
Kali Linux
Windows 11
Cisco Packet Tracer

The details of files are as follows:
Scan_Attack.pcapng - Wireshark capture of Nmap SYN stealth scan traffic, Bruteforce_Simulation.pcapng- Wireshark capture of repeated ping loop traffic, traffic_dataset.csv - Structured dataset extracted from both capture files, isolation_forest_results.csv - Isolation Forest model output with anomaly classifications, labeled_results.csv - Labeled version of the model output, pcap_to_csv.py - Script to convert pcapng files to CSV dataset, train_isolation_forest.py - Script to train and apply the Isolation Forest model, label_data.py - Script to label the model output, anomaly_summary.py - Script to generate the anomaly detection summary, Baseline_Network.pkt - Cisco Packet Tracer file for the baseline LAN topology, Hardened_LAN.pkt - Cisco Packet Tracer file for the hardened LAN topology, layer.svg - MITRE ATT&CK Navigator mapping of simulated attack techniques.
