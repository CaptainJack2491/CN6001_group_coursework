# Enterprise Cloud Architecture (ECA) Model - CVD Clinic

This document outlines the proposed Enterprise Cloud Architecture for the CVD Clinic (Case Study 4). The architecture uses Amazon Web Services (AWS) to host the Client-Server System (CSS) portal and MySQL database, securely integrating with the on-premise clinic network.

## Resolving Connectivity Problems
A key requirement of the coursework is addressing network connectivity issues. To ensure high availability and prevent connection drops between the on-premise clinic and the cloud system:
1. **Redundant Connections:** The architecture utilizes an **Active/Active AWS Site-to-Site VPN** topology. If one IPSec tunnel goes down, the second tunnel automatically handles the traffic.
2. **Multi-AZ Cloud Deployment:** The application and database tiers are deployed across two isolated Availability Zones (AZs). This means if an entire data center goes offline, the portal stays online.
3. **Content Delivery Network (CDN):** Amazon CloudFront caches static portal assets (HTML, CSS, JS) at edge locations close to the patients, ensuring fast load times even on slow home connections.

## Architecture Diagram (Mermaid JS)

```mermaid
architecture-beta
    group onprem(cloud)[On-Premise CVD Clinic]
    
    service staff(server)[Clinic PCs/Tablets] in onprem
    service switch(switch)[Local Switch] in onprem
    service router(router)[Customer Gateway Firewall] in onprem
    
    staff:R --> L:switch
    switch:R --> L:router

    group aws(cloud)[AWS Cloud (eu-west-2)]
    
    service vgw(server)[Virtual Private Gateway] in aws
    service waf(server)[AWS WAF & CloudFront] in aws
    service igw(internet)[Internet Gateway] in aws
    
    router:R -- IPsec VPN Tunnels --> L:vgw
    
    group vpc(cloud)[Virtual Private Cloud VPC] in aws
    
    group az1(cloud)[Availability Zone A] in vpc
    group az2(cloud)[Availability Zone B] in vpc

    service alb1(server)[Application Load Balancer] in az1
    service alb2(server)[Application Load Balancer] in az2
    
    service web1(server)[Web Servers EC2 AutoScaling] in az1
    service web2(server)[Web Servers EC2 AutoScaling] in az2

    service db1(database)[Amazon RDS MySQL Primary] in az1
    service db2(database)[Amazon RDS MySQL Standby] in az2

    alb1:B --> T:web1
    alb2:B --> T:web2
    
    web1:B --> T:db1
    web2:B --> T:db2

    db1:R -- Sync Replication --> L:db2
    alb1:R -- Active/Active --> L:alb2

    waf:B --> T:igw
    igw:B --> T:alb1
    vgw:B --> T:web1
```

## Generated SVG Option
If you need this architecture exported directly as a raw SVG image file for your final report, you can execute the Python script located at `scripts/generate_eca_diagram.py`. It uses the Python `diagrams` library to construct a high-quality SVG node graph of this exact topology.
