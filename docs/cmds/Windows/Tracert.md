## Tracert

```sh
F:\>tracert google.com

Tracing route to google.com [142.250.189.14]
over a maximum of 30 hops:

  1   172 ms   182 ms   183 ms  connect.ios.astrill.com [198.18.0.1]
  2   172 ms   179 ms   174 ms  23-94-235-245-host.colocrossing.com [23.94.235.245]
  3   173 ms   188 ms   242 ms  10.9.11.241
  4   173 ms   173 ms   174 ms  lax-b22-link.ip.twelve99.net [62.115.146.158]
  5   174 ms   182 ms   176 ms  google-ic-344098.ip.twelve99-cust.net [62.115.174.31]
  6   174 ms   173 ms   174 ms  142.251.226.187
  7   175 ms   176 ms   172 ms  142.251.60.131
  8   172 ms   176 ms   184 ms  lax31s16-in-f14.1e100.net [142.250.189.14]

Trace complete.
```

```sh
F:\>tracert -d google.com

Tracing route to google.com [142.250.189.14]
over a maximum of 30 hops:

  1   173 ms   175 ms   176 ms  198.18.0.1
  2   173 ms   174 ms   175 ms  23.94.235.245
  3   179 ms   173 ms   176 ms  10.9.11.241
  4   178 ms   174 ms   174 ms  62.115.146.158
  5   176 ms   179 ms   174 ms  62.115.174.31
  6   174 ms   176 ms   176 ms  142.251.226.187
  7   173 ms   181 ms   175 ms  142.251.60.131
  8   174 ms   177 ms   173 ms  142.250.189.14

Trace complete.
```