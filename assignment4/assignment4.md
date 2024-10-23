

| **Prefix (Binary)**                       | **Prefix Length** | **Link Interface** |
|-------------------------------------------|-------------------|--------------------|
| 11110100 000                              | /11               | 0                  |
| 11110100 00100000 0                       | /17               | 1                  |
| 11110100                                  | /8                | 2                  |
| otherwise                                 |                   | 3                  |

### Explanation:

- **Link 0**: The prefix `11110100 000` (11 bits) matches the range `11110100 00000000 00000000 00000000` to `11110100 00011111 11111111 11111111`.
- **Link 1**: The prefix `11110100 00100000 0` (17 bits) matches the range `11110100 00100000 00000000 00000000` to `11110100 00100000 01111111 11111111`.
- **Link 2**: The prefix `11110100` (8 bits) matches all addresses starting with `11110100`, covering the range `11110100 00100000 10000000 00000000` to `11110100 10111111 11111111 11111111`.
- **Otherwise**: Any address not matching the above prefixes will be forwarded to **Link 3**.



### 2. Determining the Appropriate Link Interface for Datagrams:

#### a) **11100100 10010001 01010001 01010101**
   - **Prefix matching**: The address `11100100 10010001 01010001 01010101` starts with `11100100`, which does **not** match any of the prefixes `11110100` in the table.
   - **Link Interface**: Since no match is found, it falls into the "otherwise" case.
   - **Result**: **Link 3**

#### b) **11110100 10100000 11000011 00111100**
   - **Prefix matching**: The address starts with `11110100 101`, which matches the prefix `11110100` with /8 length (entry for **Link 2**).
   - **Result**: **Link 2**

#### c) **11110100 11000000 00010001 01110111**
   - **Prefix matching**: The address starts with `11110100 110`, which matches the prefix `11110100` with /8 length (entry for **Link 2**).
   - **Result**: **Link 2**

#### d) **11110100 10000011 11000001 00101100**
   - **Prefix matching**: The address starts with `11110100 100`, which matches the prefix `11110100` with /8 length (entry for **Link 2**).
   - **Result**: **Link 2**

### Summary of Results:
- **a)** goes to **Link 3** (no match, default route).
- **b)**, **c)**, and **d)** all go to **Link 2** (matching prefix `11110100` /8).

This process ensures each datagram is forwarded to the appropriate link interface based on the longest prefix match from the forwarding table.


 ### a. **How many subnets are there in this topology?**

To determine the number of subnets in this topology:
- **5 subnets**: Subnets A, B, C, D, and E correspond to the end devices, each requiring a specific number of interfaces.
- **6 subnets**: Router-to-router connections, as there are six point-to-point links between the routers.

Thus, there are **11 subnets** in total: 5 for end devices and 6 for router-to-router connections.

---

### b. **Assign network addresses to each of these subnets**:

We are given the network block **218.85.240.0/20**, which contains 4096 IP addresses. We need to allocate subnets based on the interface requirements and list the addresses in the form **a.b.c.d/x** or **(a.b.c.d/x minus e.f.g.h/y)**.

### Full Subnet Allocation in Minus Form:

#### 1. **Subnet A (450 interfaces)**:
- **Required**: 450 interfaces
- **Closest power of 2**: 512 addresses
- **Subnet size**: **/23** (512 addresses)
- **Allocation**: `218.85.240.0/23`
  - **IP range**: `218.85.240.0` to `218.85.241.195`
  - **Minus form**: None (first subnet)

#### 2. **Subnet B (900 interfaces)**:
- **Required**: 900 interfaces
- **Closest power of 2**: 1024 addresses
- **Subnet size**: **/22** (1024 addresses)
- **Allocation**: `218.85.242.0/22`
  - **IP range**: `218.85.242.0` to `218.85.245.255`


#### 3. **Subnet C (800 interfaces)**:
- **Required**: 800 interfaces
- **Closest power of 2**: 1024 addresses
- **Subnet size**: **/22** (1024 addresses)
- **Allocation**: `218.85.246.0/22`
  - **IP range**: `218.85.246.0` to `218.85.249.255`


#### 4. **Subnet D (950 interfaces)**:
- **Required**: 950 interfaces
- **Closest power of 2**: 1024 addresses
- **Subnet size**: **/22** (1024 addresses)
- **Allocation**: `218.85.250.0/22`
  - **IP range**: `218.85.250.0` to `218.85.253.255`


#### 5. **Subnet E (480 interfaces)**:
- **Required**: 480 interfaces
- **Closest power of 2**: 512 addresses
- **Subnet size**: **/23** (512 addresses)
- **Allocation**: `218.85.254.0/23`
  - **IP range**: `218.85.254.0` to `218.85.255.255`


### Router-to-Router Link Allocations in Minus Form:

#### **R1-R2 Link**:
- **Required**: 2 interfaces
- **Subnet size**: **/30** (4 addresses)
- **Allocation**: `218.85.241.196/30`
  - **IP range**: `218.85.241.196` to `218.85.241.199`
  - **Minus form**: `218.85.241.196/23 minus 218.85.241.196/30`

#### **R1-R3 Link**:
- **Required**: 2 interfaces
- **Subnet size**: **/30** (4 addresses)
- **Allocation**: `218.85.241.200/30`
  - **IP range**: `218.85.241.200` to `218.85.241.203`

#### **R1-R4 Link**:
- **Required**: 2 interfaces
- **Subnet size**: **/30** (4 addresses)
- **Allocation**: `218.85.241.204/30`
  - **IP range**: `218.85.241.204` to `218.85.241.207`

#### **R2-R3 Link**:
- **Required**: 2 interfaces
- **Subnet size**: **/30** (4 addresses)
- **Allocation**: `218.85.241.208/30`
  - **IP range**: `218.85.241.208` to `218.85.241.211`

#### **R3-R4 Link**:
- **Required**: 2 interfaces
- **Subnet size**: **/30** (4 addresses)
- **Allocation**: `218.85.241.212/30`
  - **IP range**: `218.85.241.212` to `218.85.241.215`

#### **R2-R4 Link**:
- **Required**: 2 interfaces
- **Subnet size**: **/30** (4 addresses)
- **Allocation**: `218.85.241.216/30`
  - **IP range**: `218.85.241.216` to `218.85.241.219`



### Final Summary of All Subnet Allocations:

| **Subnet**        | **Subnet Allocation**              | **IP Range**                              |
|-------------------|------------------------------------|-------------------------------------------|
| **Subnet A**      | `218.85.240.0/23`                  | `218.85.240.0` to `218.85.241.195`        |
| **Subnet B**      | `218.85.242.0/22`                  | `218.85.242.0` to `218.85.245.255`        |
| **Subnet C**      | `218.85.246.0/22`                  | `218.85.246.0` to `218.85.249.255`        |
| **Subnet D**      | `218.85.250.0/22`                  | `218.85.250.0` to `218.85.253.255`        |
| **Subnet E**      | `218.85.254.0/23`                  | `218.85.254.0` to `218.85.255.255`        |
| **R1-R2 Link**    | `218.85.241.196/30`                | `218.85.241.196` to `218.85.241.199`      |
| **R1-R3 Link**    | `218.85.241.200/30`                | `218.85.241.200` to `218.85.241.203`      |
| **R1-R4 Link**    | `218.85.241.204/30`                | `218.85.241.204` to `218.85.241.207`      |
| **R2-R3 Link**    | `218.85.241.208/30`                | `218.85.241.208` to `218.85.241.211`      |
| **R3-R4 Link**    | `218.85.241.212/30`                | `218.85.241.212` to `218.85.241.215`      |
| **R2-R4 Link**    | `218.85.241.216/30`                | `218.85.241.216` to `218.85.241.219`      |

