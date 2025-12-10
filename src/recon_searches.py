"""
Reconnaissance search functions for BigBountyRecon
All functions open URLs in Chrome browser
"""

import webbrowser
import urllib.parse


def get_chrome_browser():
    """Get Chrome browser controller, fallback to default if Chrome not available"""
    import platform
    
    # Try different Chrome browser names based on platform
    chrome_names = ['chrome', 'google-chrome', 'chromium', 'chromium-browser']
    
    for name in chrome_names:
        try:
            chrome = webbrowser.get(name)
            return chrome
        except webbrowser.Error:
            continue
    
    # If Chrome not found, try to register it manually on macOS
    if platform.system() == 'Darwin':
        import subprocess
        chrome_paths = [
            '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
            '/Applications/Chromium.app/Contents/MacOS/Chromium'
        ]
        for path in chrome_paths:
            try:
                webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(path))
                return webbrowser.get('chrome')
            except:
                continue
    
    # Fallback to default browser
    return webbrowser


def open_url(url):
    """Open URL in Chrome browser"""
    browser = get_chrome_browser()
    browser.open(url)


def directory_listing(domain):
    """Directory Listing: Finding open directories"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} intitle:index.of"
    open_url(url)


def configuration_files(domain):
    """Configuration Files: Often contains sensitive information"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini"
    open_url(url)


def database_files(domain):
    """Database Files: Data files that store database contents"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} ext:sql | ext:dbf | ext:mdb"
    open_url(url)


def wordpress(domain):
    """WordPress: WordPress related exposure"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} inurl:wp- | inurl:wp-content | inurl:plugins | inurl:uploads | inurl:themes | inurl:download"
    open_url(url)


def log_files(domain):
    """Log Files: Sometimes provide detailed information"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} ext:log"
    open_url(url)


def backup_files(domain):
    """Backup and Old Files: Backup files are original copies"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"
    open_url(url)


def login_pages(domain):
    """Login Pages: Identify login pages"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} inurl:login | inurl:signin | intitle:Login | intitle: signin | inurl:auth"
    open_url(url)


def documents(domain):
    """Publicly Exposed Documents: Can be used to extract metadata"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} ext:doc | ext:docx | ext:odt | ext:pdf | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"
    open_url(url)


def phpinfo(domain):
    """phpinfo(): Exposing phpinfo()"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} ext:php intitle:phpinfo \"published by the PHP Group\""
    open_url(url)


def backdoors(domain):
    """Finding Backdoors: Identify website defacements"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)}  inurl:shell | inurl:backdoor | inurl:wso | inurl:cmd | shadow | passwd | boot.ini | inurl:backdoor"
    open_url(url)


def install_setup_files(domain):
    """Install/Setup Files: Allows enumeration"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)}  inurl:readme | inurl:license | inurl:install | inurl:setup | inurl:config"
    open_url(url)


def sql_errors(domain):
    """SQL Errors: SQL errors leak sensitive information"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} intext:\"sql syntax near\" | intext:\"syntax error has occurred\" | intext:\"incorrect syntax near\" | intext:\"unexpected end of SQL command\" | intext:\"Warning: mysql_connect()\" | intext:\"Warning: mysql_query()\" | intext:\"Warning: pg_connect()\""
    open_url(url)


def open_redirects(domain):
    """Open Redirects: Look at various known parameters"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http"
    open_url(url)


def apache_struts(domain):
    """Apache Struts RCE: Looking for files with extensions .action or .do"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} ext:action | ext:struts | ext:do"
    open_url(url)


def pastebin(domain):
    """Find Pastebin Entries: Results related to target organisation"""
    url = f"https://www.google.com/search?q=site:pastebin.com {urllib.parse.quote(domain)}"
    open_url(url)


def linkedin_employees(domain):
    """Employees on LINKEDIN: Identifying employee names"""
    url = f"https://www.google.com/search?q=site:linkedin.com employees {urllib.parse.quote(domain)}"
    open_url(url)


def sharepoint_rce(domain):
    """SharePoint RCE: Look for CVE-2020-0646 SharePoint RCE"""
    url = f"https://www.google.com/search?q=.sharepoint.com/_vti_bin/webpartpages/asmx -docs -msdn -mdsec site:{urllib.parse.quote(domain)}"
    open_url(url)


def wsdl_files(domain):
    """API Endpoints: Find WSDL files"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} filetype:wsdl | filetype:WSDL | ext:svc | inurl:wsdl | Filetype: ?wsdl | inurl:asmx?wsdl | inurl:jws?wsdl | intitle:_vti_bin/sites.asmx?wsdl | inurl:_vti_bin/sites.asmx?wsdl"
    open_url(url)


def github(domain):
    """GitHub: Quickly look for sensitive information"""
    quote = "\""
    asterisk = "*."
    url = f"https://github.com/search?q={quote}{asterisk}{urllib.parse.quote(domain)}{quote}"
    open_url(url)


def gist(domain):
    """Gist Searches: Quickly look for sensitive information"""
    quote = "\""
    url = f"https://gist.github.com/search?q=*.{quote}{urllib.parse.quote(domain)}{quote}"
    open_url(url)


def apache_config(domain):
    """Apache Config Files: Apache HTTP Server configuration"""
    quote = "\""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} filetype:config {quote}apache{quote}"
    open_url(url)


def third_party_exposure(domain):
    """3rd Party Exposure: Exposure on third party sites"""
    quote = "\""
    url = f"https://www.google.com/search?q=site%3Ahttp%3A%2F%2Fideone.com+|+site%3Ahttp%3A%2F%2Fcodebeautify.org+|+site%3Ahttp%3A%2F%2Fcodeshare.io+|+site%3Ahttp%3A%2F%2Fcodepen.io+|+site%3Ahttp%3A%2F%2Frepl.it+|+site%3Ahttp%3A%2F%2Fjustpaste.it+|+site%3Ahttp%3A%2F%2Fpastebin.com+|+site%3Ahttp%3A%2F%2Fjsfiddle.net+|+site%3Ahttp%3A%2F%2Ftrello.com+|+site%3A*.atlassian.net+|+site%3Abitbucket.org+ {quote}{urllib.parse.quote(domain)}{quote}"
    open_url(url)


def bitbucket_atlassian(domain):
    """BitBucket & Atlassian: Source code leakage"""
    quote = "\""
    url = f"https://www.google.com/search?q=site%3Aatlassian.net+|+site%3Abitbucket.org+ {quote}{urllib.parse.quote(domain)}{quote}"
    open_url(url)


def git_folder(domain):
    """git Folder: Source code exposure"""
    quote = "\""
    url = f"https://www.google.com/search?q=inurl:{quote}/.git {quote} {urllib.parse.quote(domain)} -github "
    open_url(url)


def traefik(domain):
    """Traefik: Look for open-source Edge Router"""
    quote = "\""
    url = f"https://www.google.com/search?q=intitle:traefik+inurl:8080/dashboard{quote}{urllib.parse.quote(domain)}{quote}"
    open_url(url)


def ct_logs(domain):
    """CT Logs: Certificate Transparency logs"""
    url = f"https://crt.sh/?q={urllib.parse.quote(domain)}"
    open_url(url)


def htaccess_phpinfo(domain):
    """.HTACCESS / Sensitive Files: Look for sensitive file exposure"""
    quote = "\""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} inurl:{quote}/phpinfo.php{quote} | inurl:{quote}.htaccess{quote}"
    open_url(url)


def subdomains(domain):
    """Find Subdomains: Subdomain helps expand attack surface"""
    asterisk = "*."
    url = f"https://www.google.com/search?q=site:{asterisk}{urllib.parse.quote(domain)}"
    open_url(url)


def sub_subdomains(domain):
    """Find Sub-Subdomains: Identify sub-sub domains"""
    asterisk = "*.*."
    url = f"https://www.google.com/search?q=site:{asterisk}{urllib.parse.quote(domain)}"
    open_url(url)


def wordpress_exposure(domain):
    """Find WordPress related exposure: WordPress related exposure"""
    url = f"https://www.google.com/search?q=site:{urllib.parse.quote(domain)} inurl:wp-content | inurl:wp-includes"
    open_url(url)


def wordpress_wayback(domain):
    """Find WordPress related exposure using Wayback Machine"""
    url = f"http://wwwb-dedup.us.archive.org:8083/cdx/search?url={urllib.parse.quote(domain)}/&matchType=domain&collapse=digest&output=text&fl=original,timestamp&filter=urlkey:.*wp[-].*&limit=1000000&xx="
    open_url(url)


def openbugbounty(domain):
    """OpenBugBounty: Look for publicly exposed security issues"""
    url = f"https://www.openbugbounty.org/search/?search={urllib.parse.quote(domain)}"
    open_url(url)


def reddit(domain):
    """Reddit: Information about organisation on Reddit"""
    url = f"https://www.reddit.com/search/?q={urllib.parse.quote(domain)}"
    open_url(url)


def crossdomain_xml(domain):
    """Crossdomain.xml: Look for misconfigured crossdomain.xml files"""
    url = f"https://www.google.com/search?q={urllib.parse.quote(domain)}/crossdomain.xml"
    open_url(url)


def robots_txt(domain):
    """Robots.txt File: Instructs web robots how to crawl"""
    url = f"https://www.google.com/search?q={urllib.parse.quote(domain)}/robots.txt"
    open_url(url)


def security_headers(domain):
    """Check Security Headers: Identify security related headers"""
    url = f"https://securityheaders.com/?q={urllib.parse.quote(domain)}&followRedirects=on"
    open_url(url)


def threatcrowd(domain):
    """ThreatCrowd: Search engine for threats"""
    url = f"https://threatcrowd.org/domain.php?domain={urllib.parse.quote(domain)}"
    open_url(url)


def riskiq(domain):
    """RiskIQ: Threat investigation"""
    url = f"https://community.riskiq.com/search/{urllib.parse.quote(domain)}"
    open_url(url)


def swf_google(domain):
    """.SWF File (Google): Look for older versions of flash .swf"""
    url = f"https://www.google.com/search?q=inurl:{urllib.parse.quote(domain)} ext:swf"
    open_url(url)


def youtube(domain):
    """YouTube: Look for any recent news"""
    url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(domain)}"
    open_url(url)


def swf_yandex(domain):
    """.SWF File (Yandex): Look for older versions of flash .swf"""
    url = f"https://yandex.com/search/?text=site:{urllib.parse.quote(domain)}  mime:swf"
    open_url(url)


def swf_wayback(domain):
    """.SWF File (Wayback Machine): Look for older versions of flash .swf"""
    url = f"https://web.archive.org/cdx/search?url={urllib.parse.quote(domain)}/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=urlkey:.*swf&limit=100000"
    open_url(url)


def swf_wayback_mime(domain):
    """.SWF File (Wayback Machine MIME): Look for older versions of flash .swf"""
    url = f"https://web.archive.org/cdx/search?url={urllib.parse.quote(domain)}/&matchType=domain&collapse=urlkey&output=text&fl=original&filter=mimetype:application/x-shockwave-flash&limit=100000"
    open_url(url)


def wayback_machine(domain):
    """Wayback Machine: Look for archived files"""
    url = f"https://web.archive.org/web/*/{urllib.parse.quote(domain)}/*"
    open_url(url)


def reverse_ip(domain):
    """Reverse IP Lookup: Discover all domain names hosted on IP"""
    url = f"https://viewdns.info/reverseip/?host={urllib.parse.quote(domain)}&t=1"
    open_url(url)


def publicwww(domain):
    """PublicWWW: Source code search engine"""
    quote = "\""
    url = f"https://publicwww.com/websites/{quote}{urllib.parse.quote(domain)}{quote}/"
    open_url(url)


def censys_ipv4(domain):
    """Censys (IPv4): Search engine for finding internet devices"""
    url = f"https://censys.io/ipv4?q={urllib.parse.quote(domain)}"
    open_url(url)


def censys_domain(domain):
    """Censys (Domain): Search engine for finding internet devices"""
    url = f"https://censys.io/domain?q={urllib.parse.quote(domain)}"
    open_url(url)


def censys_certificates(domain):
    """Censys (Certificates): Search engine for finding internet devices"""
    url = f"https://censys.io/certificates?q={urllib.parse.quote(domain)}"
    open_url(url)


def shodan(domain):
    """Shodan: Search engine for Internet-connected devices"""
    url = f"https://www.shodan.io/search?query={urllib.parse.quote(domain)}"
    open_url(url)


def google_cse(domain):
    """Google CSE: Custom search engine"""
    url = f"https://cse.google.com/cse?cx=002972716746423218710:veac6ui3rio#gsc.tab=0&gsc.q={urllib.parse.quote(domain)}"
    open_url(url)


def throwbin(domain):
    """Throwbin: Look for sensitive information"""
    url = f"https://www.google.com/search?q=site:throwbin.io {urllib.parse.quote(domain)}"
    open_url(url)


def domaineye(domain):
    """DomainEye: Domain/host investigation tool"""
    url = f"https://domaineye.com/similar/{urllib.parse.quote(domain)}"
    open_url(url)


def gitlab(domain):
    """GitLab: Quickly look for sensitive information"""
    url = f"https://www.google.com/search?q=inurl:gitlab {urllib.parse.quote(domain)}"
    open_url(url)


def stackoverflow(domain):
    """Stackoverflow: Source code exposure"""
    quote = "\""
    url = f"https://www.google.com/search?q=site:stackoverflow.com {quote}{urllib.parse.quote(domain)}{quote}"
    open_url(url)


def s3_buckets(domain):
    """s3 Buckets: Open s3 buckets"""
    quote = "\""
    url = f"https://www.google.com/search?q=site:.s3.amazonaws.com {quote}{urllib.parse.quote(domain)}{quote}"
    open_url(url)


def digitalocean_spaces(domain):
    """Digitalocean Spaces: S3-compatible object storage"""
    quote = "\""
    url = f"https://www.google.com/search?q=site:digitaloceanspaces.com {quote}{urllib.parse.quote(domain)}{quote}"
    open_url(url)


def whatcms(domain):
    """What CMS: Identify the version and type of CMS"""
    url = f"https://whatcms.org/?s={urllib.parse.quote(domain)}"
    open_url(url)
