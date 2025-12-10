"""
BigBountyRecon - Python Tkinter Version
Reconnaissance tool with 58+ techniques using Google dorks and open source tools
"""

import tkinter as tk
from tkinter import ttk, messagebox
import recon_searches

# Set to True to use the old categorized UI, False for the new grid layout matching original
use_old_ui = False


class BigBountyReconApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BigBountyRecon")
        
        if use_old_ui:
            self.create_old_ui()
        else:
            self.create_new_ui()
    
    def validate_and_run(self, func):
        """Validate domain input and run the function"""
        domain = self.domain_entry.get().strip()
        if not domain:
            messagebox.showwarning("Warning", "Please enter a target domain")
            return
        func(domain)
    
    def create_new_ui(self):
        """Create the new UI matching the original Windows Forms layout"""
        self.root.geometry("1400x850")
        self.root.configure(bg="#F0F0F0")
        self.root.minsize(1200, 700)
        
        # Make root resizable
        self.root.rowconfigure(2, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        # Header with logo
        header_frame = tk.Frame(self.root, bg="#F0F0F0", pady=8)
        header_frame.pack(fill=tk.X)
        
        # Logo text
        logo_label = tk.Label(header_frame, text="BIG BOUNTY RECON", 
                             font=("Arial", 24, "bold"), 
                             fg="#000000", bg="#F0F0F0")
        logo_label.pack()
        
        # Domain input
        input_frame = tk.Frame(self.root, bg="#F0F0F0", pady=8)
        input_frame.pack(fill=tk.X, padx=20)
        
        self.domain_entry = tk.Entry(input_frame, width=50, font=("Arial", 16), 
                                    relief=tk.SOLID, borderwidth=1)
        self.domain_entry.pack(expand=True, padx=5)
        self.domain_entry.insert(0, "tesla.com")
        self.domain_entry.bind('<Return>', lambda e: self.validate_and_run(recon_searches.directory_listing))
        
        # Main button grid container - no scrollbars, direct frame, reduced padding
        main_container = tk.Frame(self.root, bg="#F0F0F0")
        main_container.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        main_container.rowconfigure(0, weight=1)
        main_container.columnconfigure(0, weight=1)
        
        # Create buttons in grid layout matching original
        self.create_new_button_grid(main_container)
    
    def create_button_with_icon(self, parent, icon, text, func, row, col):
        """Create button with icon and text - flexible sizing with text wrapping"""
        # Create button with icon on top, text below
        btn_text = f"{icon}\n{text}" if icon else text
        
        # Calculate wraplength based on estimated button width (approximately 90-100 pixels per column)
        # Subtract some padding for icon and margins
        estimated_width = 90
        wraplength = max(60, estimated_width - 20)  # Ensure minimum wraplength
        
        btn = tk.Button(parent, text=btn_text, 
                       command=lambda: self.validate_and_run(func),
                       font=("Arial", 12, "normal"),
                       relief=tk.RAISED, borderwidth=1,
                       bg="#FFFFFF", fg="#000000",
                       justify=tk.CENTER,
                       anchor=tk.CENTER,
                       wraplength=wraplength)
        btn.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
        
        # Bind to configure event to update wraplength when button is resized
        def update_wraplength(event):
            # Update wraplength to be slightly less than button width
            new_wraplength = max(60, event.width - 20)
            btn.config(wraplength=new_wraplength)
        
        btn.bind('<Configure>', update_wraplength)
        return btn
    
    def create_new_button_grid(self, parent):
        """Create button grid with 12 columns - simple layout, no sorting"""
        # Configure grid columns (12 columns: 0-11)
        for i in range(12):
            parent.columnconfigure(i, weight=1, uniform="button_col", minsize=90)
        
        # Define all buttons in order (as they appear in recon_searches.py)
        buttons = [
            ("📁", "Directory Listing", recon_searches.directory_listing),
            ("⚙️", "Configuration Files", recon_searches.configuration_files),
            ("🗄️", "Database Files", recon_searches.database_files),
            ("W", "WordPress", recon_searches.wordpress),
            ("📋", "Log Files", recon_searches.log_files),
            ("💾", "Backup and Old Files", recon_searches.backup_files),
            ("🔐", "Login Pages", recon_searches.login_pages),
            ("📄", "Publicly Exposed Documents", recon_searches.documents),
            ("🐘", "phpinfo()", recon_searches.phpinfo),
            ("🚪", "Finding Backdoors", recon_searches.backdoors),
            ("📱", "Install / Setup files", recon_searches.install_setup_files),
            ("🔧", "SQL Errors", recon_searches.sql_errors),
            ("↗️", "Open Redirects", recon_searches.open_redirects),
            ("💎", "Apache STRUTS RCE", recon_searches.apache_struts),
            ("📋", "Find Pastebin entries", recon_searches.pastebin),
            ("💼", "Employees on LINKEDIN", recon_searches.linkedin_employees),
            ("S", "CVE-2020-0646 SharePoint RCE", recon_searches.sharepoint_rce),
            ("📄", "API Endpoints - WSDL", recon_searches.wsdl_files),
            ("🐙", "Search in GITHUB", recon_searches.github),
            ("🐙", "Github GIST Searches", recon_searches.gist),
            ("⚙️", "Apache Config Files", recon_searches.apache_config),
            ("👥", "3rd Party Exposure", recon_searches.third_party_exposure),
            ("🔵", "Search in Bitbucket and Atlassian", recon_searches.bitbucket_atlassian),
            ("📁", ".git folder", recon_searches.git_folder),
            ("🔵", "Traefik", recon_searches.traefik),
            ("🔒", "Search in CT Logs", recon_searches.ct_logs),
            ("🔒", ".htaccess sensitive files", recon_searches.htaccess_phpinfo),
            ("🌍", "Find Subdomains", recon_searches.subdomains),
            ("🌍", "Find Sub-Subdomains", recon_searches.sub_subdomains),
            ("W", "Find WordPress #2", recon_searches.wordpress_exposure),
            ("🗄️", "Find WordPress [Wayback Machine]", recon_searches.wordpress_wayback),
            ("🐛", "Search in OpenBugBounty", recon_searches.openbugbounty),
            ("🤖", "Search in Reddit", recon_searches.reddit),
            ("📄", "Test CrossDomain", recon_searches.crossdomain_xml),
            ("🤖", "Robots.txt File", recon_searches.robots_txt),
            ("🛡️", "Check Security Headers", recon_searches.security_headers),
            ("🎯", "Check in ThreatCrowd", recon_searches.threatcrowd),
            ("🌀", "Passive Total", recon_searches.riskiq),
            ("F", "Find .SWF file (Google)", recon_searches.swf_google),
            ("▶️", "YouTube", recon_searches.youtube),
            ("F", "Find .SWF file (Yandex)", recon_searches.swf_yandex),
            ("F", "Search SWF in WayBack", recon_searches.swf_wayback),
            ("🌐", "Search in Wayback Machine #2", recon_searches.swf_wayback_mime),
            ("🌐", "Search in Wayback Machine #3", recon_searches.wayback_machine),
            ("🔍", "Reverse IP Lookup", recon_searches.reverse_ip),
            ("Q", "Sourcecode - PublicWWW", recon_searches.publicwww),
            ("🔍", "Check in CENSYS [IP4]", recon_searches.censys_ipv4),
            ("🔍", "Check in CENSYS [DOMAINS]", recon_searches.censys_domain),
            ("🔍", "Check in CENSYS [CERTS]", recon_searches.censys_certificates),
            ("8", "Search in SHODAN", recon_searches.shodan),
            ("☁️", "Cloud Storage and Buckets", recon_searches.google_cse),
            ("🔑", "Plaintext Password Leak", recon_searches.throwbin),
            ("👁️", "DomainEye", recon_searches.domaineye),
            ("🦊", "GitLab", recon_searches.gitlab),
            ("📚", "Search in Stackoverflow", recon_searches.stackoverflow),
            ("🪣", "s3 Buckets", recon_searches.s3_buckets),
            ("💧", "Digital Ocean Spaces", recon_searches.digitalocean_spaces),
            ("📊", "What CMS?", recon_searches.whatcms),
        ]
        
        # Calculate number of rows needed
        num_rows = (len(buttons) + 11) // 12  # Ceiling division
        
        # Configure rows
        for i in range(num_rows):
            parent.rowconfigure(i, weight=1, uniform="button_row", minsize=65)
        
        # Place buttons in grid (left to right, top to bottom)
        for index, (icon, text, func) in enumerate(buttons):
            row = index // 12
            col = index % 12
            self.create_button_with_icon(parent, icon, text, func, row, col)
    
    def create_old_ui(self):
        """Create the old categorized UI"""
        self.root.geometry("800x700")
        
        # Domain input
        input_frame = ttk.Frame(self.root, padding="10")
        input_frame.pack(fill=tk.X)
        
        ttk.Label(input_frame, text="Enter Target Domain:", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)
        self.domain_entry = ttk.Entry(input_frame, width=40, font=("Arial", 11))
        self.domain_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        self.domain_entry.bind('<Return>', lambda e: self.validate_and_run(recon_searches.directory_listing))
        
        # Create scrollable frame for buttons
        canvas = tk.Canvas(self.root)
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Create button groups
        self.create_button_groups(scrollable_frame)
    
    def create_button(self, parent, text, func, row, col, width=30):
        """Helper method to create buttons"""
        btn = ttk.Button(parent, text=text, command=lambda: self.validate_and_run(func), width=width)
        btn.grid(row=row, column=col, padx=5, pady=3, sticky="ew")
        return btn
    
    def create_button_groups(self, parent):
        """Create all button groups organized by category"""
        row = 0
        
        # File Searches Section
        file_frame = ttk.LabelFrame(parent, text="File Searches", padding="10")
        file_frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        file_frame.columnconfigure(0, weight=1)
        file_frame.columnconfigure(1, weight=1)
        
        file_row = 0
        self.create_button(file_frame, "Directory Listing", recon_searches.directory_listing, file_row, 0)
        self.create_button(file_frame, "Configuration Files", recon_searches.configuration_files, file_row, 1)
        file_row += 1
        self.create_button(file_frame, "Database Files", recon_searches.database_files, file_row, 0)
        self.create_button(file_frame, "Log Files", recon_searches.log_files, file_row, 1)
        file_row += 1
        self.create_button(file_frame, "Backup Files", recon_searches.backup_files, file_row, 0)
        self.create_button(file_frame, "Documents", recon_searches.documents, file_row, 1)
        file_row += 1
        self.create_button(file_frame, "Apache Config", recon_searches.apache_config, file_row, 0)
        self.create_button(file_frame, ".htaccess/phpinfo", recon_searches.htaccess_phpinfo, file_row, 1)
        file_row += 1
        self.create_button(file_frame, "phpinfo", recon_searches.phpinfo, file_row, 0)
        self.create_button(file_frame, "Install/Setup Files", recon_searches.install_setup_files, file_row, 1)
        file_row += 1
        self.create_button(file_frame, "Backdoors", recon_searches.backdoors, file_row, 0)
        self.create_button(file_frame, "robots.txt", recon_searches.robots_txt, file_row, 1)
        file_row += 1
        self.create_button(file_frame, "crossdomain.xml", recon_searches.crossdomain_xml, file_row, 0)
        self.create_button(file_frame, ".git Folder", recon_searches.git_folder, file_row, 1)
        
        row += 1
        
        # WordPress Section
        wp_frame = ttk.LabelFrame(parent, text="WordPress", padding="10")
        wp_frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        wp_frame.columnconfigure(0, weight=1)
        wp_frame.columnconfigure(1, weight=1)
        
        wp_row = 0
        self.create_button(wp_frame, "WordPress", recon_searches.wordpress, wp_row, 0)
        self.create_button(wp_frame, "WordPress Exposure", recon_searches.wordpress_exposure, wp_row, 1)
        wp_row += 1
        self.create_button(wp_frame, "WordPress Wayback", recon_searches.wordpress_wayback, wp_row, 0)
        
        row += 1
        
        # Authentication & Errors Section
        auth_frame = ttk.LabelFrame(parent, text="Authentication & Errors", padding="10")
        auth_frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        auth_frame.columnconfigure(0, weight=1)
        auth_frame.columnconfigure(1, weight=1)
        
        auth_row = 0
        self.create_button(auth_frame, "Login Pages", recon_searches.login_pages, auth_row, 0)
        self.create_button(auth_frame, "SQL Errors", recon_searches.sql_errors, auth_row, 1)
        auth_row += 1
        self.create_button(auth_frame, "Open Redirects", recon_searches.open_redirects, auth_row, 0)
        self.create_button(auth_frame, "Apache Struts", recon_searches.apache_struts, auth_row, 1)
        
        row += 1
        
        # Subdomains Section
        subdomain_frame = ttk.LabelFrame(parent, text="Subdomains", padding="10")
        subdomain_frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        subdomain_frame.columnconfigure(0, weight=1)
        subdomain_frame.columnconfigure(1, weight=1)
        
        sub_row = 0
        self.create_button(subdomain_frame, "Subdomains", recon_searches.subdomains, sub_row, 0)
        self.create_button(subdomain_frame, "Sub-subdomains", recon_searches.sub_subdomains, sub_row, 1)
        sub_row += 1
        self.create_button(subdomain_frame, "CT Logs (crt.sh)", recon_searches.ct_logs, sub_row, 0)
        self.create_button(subdomain_frame, "Reverse IP", recon_searches.reverse_ip, sub_row, 1)
        
        row += 1
        
        # Third-party Services Section
        thirdparty_frame = ttk.LabelFrame(parent, text="Third-party Services", padding="10")
        thirdparty_frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        thirdparty_frame.columnconfigure(0, weight=1)
        thirdparty_frame.columnconfigure(1, weight=1)
        
        tp_row = 0
        self.create_button(thirdparty_frame, "GitHub", recon_searches.github, tp_row, 0)
        self.create_button(thirdparty_frame, "Gist", recon_searches.gist, tp_row, 1)
        tp_row += 1
        self.create_button(thirdparty_frame, "GitLab", recon_searches.gitlab, tp_row, 0)
        self.create_button(thirdparty_frame, "Pastebin", recon_searches.pastebin, tp_row, 1)
        tp_row += 1
        self.create_button(thirdparty_frame, "Throwbin", recon_searches.throwbin, tp_row, 0)
        self.create_button(thirdparty_frame, "StackOverflow", recon_searches.stackoverflow, tp_row, 1)
        tp_row += 1
        self.create_button(thirdparty_frame, "LinkedIn Employees", recon_searches.linkedin_employees, tp_row, 0)
        self.create_button(thirdparty_frame, "Reddit", recon_searches.reddit, tp_row, 1)
        tp_row += 1
        self.create_button(thirdparty_frame, "YouTube", recon_searches.youtube, tp_row, 0)
        self.create_button(thirdparty_frame, "Third-party Exposure", recon_searches.third_party_exposure, tp_row, 1)
        tp_row += 1
        self.create_button(thirdparty_frame, "BitBucket & Atlassian", recon_searches.bitbucket_atlassian, tp_row, 0)
        
        row += 1
        
        # Security Tools Section
        security_frame = ttk.LabelFrame(parent, text="Security Tools", padding="10")
        security_frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        security_frame.columnconfigure(0, weight=1)
        security_frame.columnconfigure(1, weight=1)
        
        sec_row = 0
        self.create_button(security_frame, "Shodan", recon_searches.shodan, sec_row, 0)
        self.create_button(security_frame, "Censys IPv4", recon_searches.censys_ipv4, sec_row, 1)
        sec_row += 1
        self.create_button(security_frame, "Censys Domain", recon_searches.censys_domain, sec_row, 0)
        self.create_button(security_frame, "Censys Certificates", recon_searches.censys_certificates, sec_row, 1)
        sec_row += 1
        self.create_button(security_frame, "ThreatCrowd", recon_searches.threatcrowd, sec_row, 0)
        self.create_button(security_frame, "RiskIQ", recon_searches.riskiq, sec_row, 1)
        sec_row += 1
        self.create_button(security_frame, "Security Headers", recon_searches.security_headers, sec_row, 0)
        self.create_button(security_frame, "OpenBugBounty", recon_searches.openbugbounty, sec_row, 1)
        sec_row += 1
        self.create_button(security_frame, "DomainEye", recon_searches.domaineye, sec_row, 0)
        self.create_button(security_frame, "What CMS", recon_searches.whatcms, sec_row, 1)
        sec_row += 1
        self.create_button(security_frame, "PublicWWW", recon_searches.publicwww, sec_row, 0)
        self.create_button(security_frame, "Google CSE", recon_searches.google_cse, sec_row, 1)
        
        row += 1
        
        # Archive & Wayback Section
        archive_frame = ttk.LabelFrame(parent, text="Archive & Wayback", padding="10")
        archive_frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        archive_frame.columnconfigure(0, weight=1)
        archive_frame.columnconfigure(1, weight=1)
        
        arch_row = 0
        self.create_button(archive_frame, "Wayback Machine", recon_searches.wayback_machine, arch_row, 0)
        self.create_button(archive_frame, "SWF (Google)", recon_searches.swf_google, arch_row, 1)
        arch_row += 1
        self.create_button(archive_frame, "SWF (Yandex)", recon_searches.swf_yandex, arch_row, 0)
        self.create_button(archive_frame, "SWF (Wayback)", recon_searches.swf_wayback, arch_row, 1)
        arch_row += 1
        self.create_button(archive_frame, "SWF (Wayback MIME)", recon_searches.swf_wayback_mime, arch_row, 0)
        
        row += 1
        
        # Cloud Storage Section
        cloud_frame = ttk.LabelFrame(parent, text="Cloud Storage", padding="10")
        cloud_frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        cloud_frame.columnconfigure(0, weight=1)
        cloud_frame.columnconfigure(1, weight=1)
        
        cloud_row = 0
        self.create_button(cloud_frame, "S3 Buckets", recon_searches.s3_buckets, cloud_row, 0)
        self.create_button(cloud_frame, "DigitalOcean Spaces", recon_searches.digitalocean_spaces, cloud_row, 1)
        
        row += 1
        
        # API & Services Section
        api_frame = ttk.LabelFrame(parent, text="API & Services", padding="10")
        api_frame.grid(row=row, column=0, columnspan=2, sticky="ew", padx=10, pady=5)
        api_frame.columnconfigure(0, weight=1)
        api_frame.columnconfigure(1, weight=1)
        
        api_row = 0
        self.create_button(api_frame, "WSDL Files", recon_searches.wsdl_files, api_row, 0)
        self.create_button(api_frame, "SharePoint RCE", recon_searches.sharepoint_rce, api_row, 1)
        api_row += 1
        self.create_button(api_frame, "Traefik", recon_searches.traefik, api_row, 0)
        
        # Configure parent grid
        parent.columnconfigure(0, weight=1)
        parent.columnconfigure(1, weight=1)


def main():
    root = tk.Tk()
    app = BigBountyReconApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
