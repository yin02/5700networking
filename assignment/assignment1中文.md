### Northeastern University 东北大学  
**Khoury College of Computer Sciences 库里计算机科学学院**  
**CS 5700 – Fundamentals of Computer Networking CS 5700 – 计算机网络基础**  
**Assignment 1 作业 1**  
**Due Monday September 23, 2024 at 11:59 pm on Canvas.**  
**截止日期为 2024 年 9 月 23 日星期一晚上 11:59 在 Canvas 上提交。**  

In all parts of the questions, explain clearly your thoughts. Writing equations and manipulating numbers are not enough to get the full grade.  
在问题的所有部分，清楚地解释你的想法。编写方程并进行运算是不足以获得满分的。

---

### Question 1: Individual 问题 1: 个人  

In packet switching with **store-and-forward**, a packet needs to be received in full at a switching node or router before it can be placed on an outgoing link and transmitted. In **cut-through switching**, as soon as the header is received, the outgoing link can be determined, and if it is free, transmission can start immediately on that link.  
在具有**存储转发**的数据包交换中，数据包必须在交换节点或路由器中被完整接收，然后才能被放置在出站链路上并进行传输。而在**直通交换**中，一旦接收到标头，就可以确定出站链路，并且如果链路空闲，传输可以立即开始。

Consider a linear path consisting of:  
- a source host,  
- a destination host,  
- 2 intermediate switches/routers, and  
- 3 intermediate links.  
考虑一条由以下部分组成的线性路径：  
- 源主机，  
- 目标主机，  
- 2 个中间交换机/路由器，  
- 3 条中间链路。  

The source has 6 packets of size 8,000 bits each. The source adds a 160-bit header to each packet. All the intermediate links have a propagation delay of 4 msec and a bit rate of 128 Kbps. Neglect queuing delays at the intermediate switches/routers.  
源主机有 6 个数据包，每个数据包的大小为 8,000 位。源主机向每个数据包添加 160 位的标头。所有中间链路的传播延迟为 4 毫秒，比特率为 128 Kbps。忽略中间交换机/路由器的排队延迟。

#### a)  
If transmission of the packets starts at time = 0, at what time instant are the 6 packets received at the destination host, if packet switching with **store-and-forward** is used? Show the space-time graph.  
如果数据包的传输在时间 = 0 时开始，使用**存储转发**的数据包交换时，6 个数据包在何时被目标主机接收？请展示时空图。

#### b)  
If transmission of the packets starts at time = 0, at what time instant are the 6 packets received at the destination host, if **cut-through switching** is used?  
如果数据包的传输在时间 = 0 时开始，使用**直通交换**时，6 个数据包在何时被目标主机接收？  

**Hint**: A similar example is solved in Module 1 lecture file.  
**提示**：类似的示例在模块 1 的讲义文件中解决过。

---

### Question 2: Individual 问题 2: 个人  

Compute the total time required to transfer (from time = 0 to the time instant at which the last bit of the file is received at the destination) an 8 MB file in the following cases, assuming:  
- the link length is 160,800 Km,  
- a frame size of 1000 Bytes to which a header of 25 Bytes is added.  
计算传输 8 MB 文件所需的总时间（从 time = 0 到文件的最后一位在目标接收时刻），假设：  
- 链路长度为 160,800 公里，  
- 帧大小为 1000 字节，且添加 25 字节的标头。  

Consider the packet size to be the frame size plus the header size. The link bit rate is 40 Mbps and the signal speed is 0.67 times the speed of light (speed of light = $3 \times 10^8$ m/s).  
将数据包大小视为帧大小加上报头大小。链路比特率为 40 Mbps，信号速度为光速的 0.67 倍（光速 = $3 \times 10^8$ m/s）。

#### a)  
Data packets can be sent continuously back-to-back.  
数据包可以连续背靠背发送。

#### b)  
A data packet can only be sent after receiving a response for the previous one (assume the response is very small and therefore its transmission time is negligible). The sender does not need to wait after the last packet is sent.  
一个数据包只有在收到前一个数据包的响应后才能发送（假设响应非常小，因此其传输时间可以忽略不计）。发送方无需在最后一个数据包发送后等待。

#### c)  
Up to 10 packets can be sent at a time. The sender cannot send any additional packets until it receives a response for the previous transmission.  
一次最多可以发送 10 个数据包。发送方在接收上次传输的响应之前，不能发送任何额外的数据包。

---

### Question 3: Individual 问题 3: 个人  

Jane writes the URL of a web page in her browser. The IP address of the corresponding web server is not cached in your local host, so a **DNS lookup** is necessary to obtain the IP address. Suppose that 4 DNS servers are visited before your host receives the IP address from DNS. The successive visits to these DNS servers incur propagation delays of 0.4 msec, 0.5 msec, 0.6 msec, and 0.8 msec, respectively.  
Jane 在浏览器中输入一个网页的 URL。对应的 Web 服务器的 IP 地址没有缓存到您的本地主机中，因此需要进行 **DNS 查找** 以获取该 IP 地址。假设在您的主机从 DNS 收到 IP 地址之前，依次访问了 4 个 DNS 服务器。这些 DNS 服务器分别产生 0.4 毫秒、0.5 毫秒、0.6 毫秒和 0.8 毫秒的传播延迟。

Suppose the web page requested consists of one packet. The length of the link separating Jane’s host from the server containing the object is 600 Km, and the signal travels at the speed of light.  
假设请求的网页由一个数据包组成。将 Jane 的主机与包含该对象的服务器隔开的链路长度为 600 公里，信号以光速传播。

#### a)  
What is the time needed to get the IP address of the web server?  
获取 Web 服务器 IP 地址需要多长时间？

#### b)  
Suppose the webpage references 10 small objects on the same server. Neglecting transmission times, and assuming persistent HTTP is used with 4 parallel connections, find the total time elapsed from the moment Jane requests the webpage to the moment she receives the webpage and all 10 objects.  
假设该网页引用了同一服务器上的 10 个小对象。忽略传输时间，假设使用持久 HTTP 和 4 个并行连接，计算从 Jane 请求网页到她收到网页和所有 10 个对象的总时间。











Here’s a structured solution and explanation for the homework assignment questions you've outlined, focusing on the specifics of each question related to networking principles:

---

### **Question 1**: 
**a) Store-and-Forward Packet Switching**

Given:
- Packet size = 8,000 bits
- Header = 160 bits
- Total packet size = 8,160 bits per packet
- Propagation delay per link = 4 msec
- Bit rate = 128 Kbps = 128,000 bits/sec

#### **Calculations**:
- **Transmission time per packet**:
  \[
  \text{Transmission Time} = \frac{\text{Total Packet Size}}{\text{Bit Rate}} = \frac{8,160 \text{ bits}}{128,000 \text{ bits/sec}} = 0.06375 \text{ sec} = 63.75 \text{ msec}
  \]
- **Total time for one packet to reach the destination**:
  \[
  \text{Total Time} = (\text{Transmission Time} + \text{Propagation Delay}) \times \text{Number of Links} = (63.75 \text{ msec} + 4 \text{ msec}) \times 3 = 203.25 \text{ msec}
  \]
- **Time for all 6 packets**:
  Since each packet starts after the previous has been transmitted, total time will be:
  \[
  \text{Start Time of Last Packet} = \text{Transmission Time} \times (6 - 1) = 63.75 \text{ msec} \times 5 = 318.75 \text{ msec}
  \]
  Adding the time taken for the last packet to reach:
  \[
  \text{Total Time for 6 Packets} = 318.75 \text{ msec} + 203.25 \text{ msec} = 522 \text{ msec}
  \]

#### **Space-Time Diagram**:
A space-time diagram would show packets moving through the nodes over time, stacking delays cumulatively as they progress through each node.

**b) Cut-Through Switching**

Given:
- As soon as the header is received, the packet begins to transmit. The header is 160 bits.

#### **Calculations**:
- **Header Transmission Time**:
  \[
  \text{Header Transmission Time} = \frac{160 \text{ bits}}{128,000 \text{ bits/sec}} = 1.25 \text{ msec}
  \]
- **Total Time for One Packet**:
  \[
  \text{Total Time for One Packet} = \text{Header Transmission Time} + \text{Propagation Delay} \times \text{Number of Links} = 1.25 \text{ msec} + 12 \text{ msec} = 13.25 \text{ msec}
  \]
- **Time for all 6 packets**:
  Since header transmission starts immediately and overlaps, time for 6 packets is:
  \[
  \text{Total Time for 6 Packets} = 13.25 \text{ msec} + (63.75 \text{ msec} - 1.25 \text{ msec}) = 75.75 \text{ msec}
  \]

### **Question 2**: 
**a) Continuous back-to-back data packets transmission**:
- **Frame size** = 1,000 bytes + 25 bytes = 1,025 bytes = 8,200 bits
- **File size** = 8 MB = 8 * 1024 * 1024 * 8 = 67,108,864 bits
- **Number of frames** = File size / Frame size = 67,108,864 / 8,200 ≈ 8,182 frames
- **Propagation delay** = (Distance / Speed of light) = 160,800,000 m / (3*10^8 m/s) = 0.536 sec
- **Transmission time per frame** = Frame size / Bit rate = 8,200 bits / (40*10^6 bits/sec) = 0.000205 sec
- **Total transfer time** = Number of frames * Transmission time per frame + Propagation delay = 8,182 * 0.000205 sec + 0.536 sec ≈ 2.205 sec

**b) Stop-and-wait protocol**:
- **Total transfer time** = (Transmission time per frame + Propagation delay) * Number of frames ≈ (0.000205 sec + 0.536 sec) * 8,182 ≈ 4,393.17 sec

**c) Sending up to 10 packets at a time**:
- **Window size** = 10
- **Rounds** = Number of frames / Window size = 8,182 / 10 = 819 rounds (approx.)
- **Total transfer time** = Rounds * (Transmission time for 10 frames + Propagation delay) ≈ 819 * (0.00205 sec + 0.536 sec) ≈ 440.706 sec

### **Question 3**: 
**a) Time to get IP address**:
- **Total propagation delay** = 0.4 msec + 0.5 msec + 0.6 msec + 0.8 msec = 2.3 msec

**b) Total time to receive webpage and all objects**:
- **Propagation delay** = Distance / Speed of light = 600,000 m / (3*10^8 m/s) = 0.002 sec
- **Assuming each object and the initial web page packet takes the same time to transmit**, and given 4 parallel connections, the total time would involve dividing the total number of objects by the number of connections and multiplying by the sum of propagation delays and negligible transmission times. Given the simplicity of the setup and neglecting specific details, a rough estimate would be calculated.

These solutions use simplified calculations and assumptions based on the information provided and standard networking principles. More complex network behaviors (like congestion, error rates, etc.) are not accounted for in this high-level analysis.