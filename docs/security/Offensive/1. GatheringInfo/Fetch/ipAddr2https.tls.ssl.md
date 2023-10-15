```sh
┌──(root㉿docker-desktop)-[/]
└─# openssl s_client -connect 192.168.0.14:443
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN = DESKTOP-28E7H5T
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN = DESKTOP-28E7H5T
verify return:1
---
Certificate chain
 0 s:CN = DESKTOP-28E7H5T
   i:CN = DESKTOP-28E7H5T
   a:PKEY: rsaEncryption, 2048 (bit); sigalg: RSA-SHA256
   v:NotBefore: May  3 17:03:59 2023 GMT; NotAfter: Apr 30 17:03:59 2033 GMT
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIC/jCCAeagAwIBAgIQUrjPCfiAxrBHoxPW/9vg6jANBgkqhkiG9w0BAQsFADAa     
MRgwFgYDVQQDDA9ERVNLVE9QLTI4RTdINVQwHhcNMjMwNTAzMTcwMzU5WhcNMzMw     
NDMwMTcwMzU5WjAaMRgwFgYDVQQDDA9ERVNLVE9QLTI4RTdINVQwggEiMA0GCSqG     
SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDDK2ja0eIVacqaIVZWBUVuJ0uI5yh+mY9n     
i5Ipk1fonLkfiI3yheS5XRn2AeKDqFsN5fACKMhSLaEH724K+ap06Pe6dA9bIUze     
zjut5cJ1sPKr1zfM5EAncloGosFZ3WOZ8tmpz43MROMkknEbH6JprBbhjF5vIpWk     
CrA34PREvjhSEizdp0J0jsOOwjeGj90BzQH28r/rqmw5UFKOlFP0qf06smPbkflP     
C+4I8oahHH3v6jEiX7mL/oB+eCK/DsJrkHFIVGxKxyiEs/8zahWfjxkD+vYCZ9ne     
WDT0VjgR+EglySgNq/H8lLG2ub4mAICKlgH9YC9jxOLT9qTEDMUFAgMBAAGjQDA+     
MAsGA1UdDwQEAwIEMDATBgNVHSUEDDAKBggrBgEFBQcDATAaBgNVHREEEzARgg9E     
RVNLVE9QLTI4RTdINVQwDQYJKoZIhvcNAQELBQADggEBAKkB0C4Kbo1PlherNAX3     
cH2lHiFAh2YtePQocijw5pEGsJaEnUO0Jaq2pGEclnBwfShCgejhPoq/szeKmWNu     
fDpc4lUZOqJsKBGrKpdVq1rAks2gRU5Om6FNK5QNndFklzN4bS5++KgggXOYXNLU     
AFGfGMNcT1KRwu/A7v0sQV7mU6PLB2KNJCHnYjblnzC1a+NVkI/7K/yqZUcpx4MV     
+HGkP+tCKfD0zgK0QZlS7i/wp84KH4pxEvMurSBX/m6afUpCukbg5vy96nKsoK+3     
ZaNctIc+c/7I67ycVnxCGXDMq2Xq500fxC5siiA6gxLNVSULTDibq0vMHN13oQ6E     
tIg=
-----END CERTIFICATE-----
subject=CN = DESKTOP-28E7H5T
issuer=CN = DESKTOP-28E7H5T
---
No client certificate CA names sent
Peer signing digest: SHA512
Peer signature type: RSA
Server Temp Key: ECDH, prime256v1, 256 bits
---
SSL handshake has read 1456 bytes and written 549 bytes
Verification error: self-signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES128-GCM-SHA256
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES128-GCM-SHA256
    Session-ID: 527C9BE189FF66714883618AEC5C5287F8C815615310D7C43CE9A1B9F3AE2473
    Session-ID-ctx:
    Master-Key: A4D375B49C7DA69173CD452F2574F8DF232076EF802720A5E4A23C8D48982AC3ECA35D81E065A99B88BC21330AEF1A7F
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - c4 b1 a7 1b bc fe b9 d0-f0 c3 d1 b3 8a d9 70 4f   ..............pO
    0010 - f2 ac 17 f3 20 59 e9 7c-86 48 59 82 0c 72 96 56   .... Y.|.HY..r.V
    0020 - 97 16 18 8a 7b 0f 05 e1-e5 d5 bc 41 ec f3 f0 82   ....{......A....
    0030 - 41 7e f6 91 9e 39 0f 60-78 b2 52 52 f8 fe 2d b6   A~...9.`x.RR..-.
    0040 - d8 9a 41 06 b1 82 ad 39-d8 5c cd c5 ec a0 ea c2   ..A....9.\......
    0050 - 62 76 d2 33 12 87 ae 02-74 2d e3 45 27 3b 4f f9   bv.3....t-.E';O.
    0060 - bb 57 da b4 36 06 eb 65-4a 9f b7 bb f7 81 85 25   .W..6..eJ......%
    0070 - 95 27 e1 5f 43 26 5e c6-5e 75 b9 ed 98 6e 92 56   .'._C&^.^u...n.V
    0080 - 8e a6 ff 46 aa e4 1e 91-09 85 f2 a9 5c 5d c5 2f   ...F........\]./
    0090 - 96 bb c1 78 21 83 74 49-4c 2f 35 1b 8c ed 92 f5   ...x!.tIL/5.....
    00a0 - f9 62 a8 e0 81 b1 14 f0-8f 1f 24 0c 72 e7 c9 46   .b........$.r..F
    00b0 - ba e0 b3 c7 ff bc 24 8d-23 d7 3b 2b 71 c7 42 c9   ......$.#.;+q.B.

    Start Time: 1697077504
    Timeout   : 7200 (sec)
    Verify return code: 18 (self-signed certificate)
    Extended master secret: no
---

HTTP/1.1 400 Bad Request
Date: Thu, 12 Oct 2023 02:31:39 GMT
Server: Apache
X-Frame-Options: SAMEORIGIN
Content-Length: 226
Connection: close
Content-Type: text/html; charset=iso-8859-1

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>400 Bad Request</title>
</head><body>
<h1>Bad Request</h1>
<p>Your browser sent a request that this server could not understand.<br />
</p>
</body></html>
closed
```