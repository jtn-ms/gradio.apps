- Fetch
- Steal
- CRACK

```sh
#$ seoanalyze https://www.sethserver.com/ -f html > results.html

$ whatweb github.com

http://github.com [301 Moved Permanently] Country[UNITED STATES][US], IP[192.30.255.112], RedirectLocation[https://github.com/]
https://github.com/ [200 OK] Content-Language[en-US], Cookies[_gh_sess,_octo,logged_in], Country[UNITED STATES][US], Email[eyebrow-23@2x.png], HTML5, HTTPServer[GitHub.com], HttpOnly[_gh_sess,logged_in], IP[192.30.255.112], Open-Graph-Protocol[object][1401488693436528], OpenSearch[/opensearch.xml], Script[application/javascript,application/json], Strict-Transport-Security[max-age=31536000; includeSubdomains; preload], Title[GitHub: Let’s build from here · GitHub], UncommonHeaders[x-content-type-options,referrer-policy,content-security-policy,x-github-request-id], X-Frame-Options[deny], X-XSS-Protection[0]
```

```sh
$ webanalyze -host www.github.com  -crawl 1
 :: webanalyze        : v0.3.9
 :: workers           : 4
 :: technologies      : technologies.json
 :: crawl count       : 1
 :: search subdomains : true
 :: follow redirects  : false

https://docs.github.com (1.8s):
    Azure Front Door,  (Load balancers)
    Azure,  (PaaS)
    Varnish,  (Caching)
    Next.js,  (JavaScript frameworks, Web frameworks, Web servers, Static site generator)
    React,  (JavaScript frameworks)
    Webpack,  (Miscellaneous)
    Node.js,  (Programming languages)
    HSTS,  (Security)
    Azure Edge Network,  (Miscellaneous)
http://github.com (3.2s):
    GitHub Pages,  (PaaS)
    HSTS,  (Security)
    Amazon S3,  (CDN)
    Amazon Web Services,  (PaaS)
```

```bash
wapiti -u 
```