# Path to hosts file
HOSTS_FILE = '/etc/hosts'

# Path to site configs
APACHE_SITE_CONFIGS_DIR = '/etc/apache2/sites-available'

# Path to activated site configs (links)
APACHE_ACTIVATED_SITE_CONFIGS_DIR = '/etc/apache2/sites-enabled'

# Path where locates all domains
DOMAINS_DIR = '/var/www'

# IP address of domain
IP_ADDRESS = '127.0.0.1'

# Extension which will stay in index file
INDEX_FILE_EXTENSION = 'php'

# Path to html template file
HTML_TEMPLATE_FILE = 'resources/html_template.html'

# Path to apache config template file
APACHE_CONFIG_TEMPLATE_FILE = 'resources/apache_config_template.txt'

# Path to htaccess file (template)
HTACCESS_FILE = 'resources/htaccess.txt'

# Ignored configs which will not view when calling "ls" command
LS_IGNORED_CONFIGS = ('000-default.conf', 'default-ssl.conf')
