# Latency test results
Python timeit module was used for all tests, in seconds.

### Code only
0.0002273210000112158  
0.0002552189999960319  
0.00022430200010603585  

Average (seconds) = 0.000235614000038  
Average (ms)      = 0.235614000037761  

### Execution only
0.0030008109997652355  
0.002957235999929253  
0.0030000189999555005  

Average (seconds) = 0.002986021999883  
Average (ms)      = 2.98602199988333  

### Code + execution
0.003391340000234777  
0.003953264999836392  
0.003240939000079379  

Average (seconds) = 0.003528514666717  
Average (ms)      = 3.52851466671685  

### Code + API + execution
0.5167385989999502  
0.4969993610000074  
0.5518439990000843  

Average (seconds) = 0.521860653000014  
Average (ms)      = 521.860653000014  

### Ping API
    PING 54.239.29.167 (54.239.29.167) 56(84) bytes of data.  
    64 bytes from 54.239.29.167: icmp_seq=1 ttl=234 time=74.2 ms  
    64 bytes from 54.239.29.167: icmp_seq=2 ttl=234 time=67.8 ms  
    64 bytes from 54.239.29.167: icmp_seq=3 ttl=234 time=76.2 ms  
    64 bytes from 54.239.29.167: icmp_seq=4 ttl=234 time=70.1 ms  
    64 bytes from 54.239.29.167: icmp_seq=5 ttl=234 time=75.0 ms  
    64 bytes from 54.239.29.167: icmp_seq=6 ttl=234 time=71.1 ms  
    64 bytes from 54.239.29.167: icmp_seq=7 ttl=234 time=74.2 ms  
    --- 54.239.29.167 ping statistics ---  
    7 packets transmitted, 7 received, 0% packet loss, time 6008ms  
    rtt min/avg/max/mdev = 67.838/72.713/76.297/2.847 ms  

## Results
There is a small discrepancy between code and execution times. There is a major difference between the network speed, execution, and the time it takes to interact with the API.

## Conclusion
There are a few factors that come into account with the timing. One is that most of the code in the `evaluate()` function was commented out and the `get_prediction()` and `get_input()` functions were not called at all.

While somewhat understandable this is definitely the range of unacceptable latency and would be highly noticeable. 
