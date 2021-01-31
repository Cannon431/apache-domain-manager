import os
import os.path
from shutil import rmtree
from glob import glob

from constants import *
from exceptions import DomainExistError, DomainNotExistError


def create(domain):
    domain_dir = DOMAINS_DIR + '/' + domain

    if os.path.exists(domain_dir):
        raise DomainExistError('Domain "' + domain + '" already exists!')

    os.makedirs(domain_dir)

    with open(domain_dir + '/index.' + INDEX_FILE_EXTENSION, 'w') as f:
        html_template = get_html_template()
        html_template = html_template.replace('{domain}', domain)

        f.write(html_template)

    with open(domain_dir + '/.htaccess', 'w') as f:
        htaccess = get_htaccess()

        f.write(htaccess)

    with open(APACHE_SITE_CONFIGS_DIR + '/' + domain + '.conf', 'w') as f:
        apache_config_template = get_apache_config_template()
        apache_config_template = apache_config_template.replace('{domain}', domain)

        f.write(apache_config_template)
    os.system('sudo a2ensite ' + domain + '.conf')
    os.system('sudo service apache2 restart')

    with open(HOSTS_FILE, 'a') as f:
        f.write('\n' + IP_ADDRESS + ' ' + domain)

    os.system('sudo chmod -R 777 ' + domain_dir)

    print('\033[92m Domain "{}" successfully created!'.format(domain))


def remove(domain):
    domain_dir = DOMAINS_DIR + '/' + domain

    if not os.path.isfile('{}/{}.conf'.format(APACHE_SITE_CONFIGS_DIR, domain)):
        raise DomainNotExistError('Domain "' + domain + '" not exists!')

    if os.path.exists(domain_dir):
        rmtree(domain_dir)

    os.unlink('{}/{}.conf'.format(APACHE_ACTIVATED_SITE_CONFIGS_DIR, domain))
    os.remove('{}/{}.conf'.format(APACHE_SITE_CONFIGS_DIR, domain))

    os.system('sudo service apache2 restart')

    print('\033[92m Domain "{}" successfully removed!'.format(domain))


def ls():
    configs = glob(APACHE_SITE_CONFIGS_DIR + '/*.conf')
    configs = [os.path.basename(config) for config in configs if os.path.basename(config) not in LS_IGNORED_CONFIGS]

    print('Domains({}):\n'.format(len(configs)))

    for config in configs:
        print(config.replace('.conf', ''))


def get_html_template():
    with open(HTML_TEMPLATE_FILE) as f:
        return f.read()


def get_apache_config_template():
    with open(APACHE_CONFIG_TEMPLATE_FILE) as f:
        return f.read()


def get_htaccess():
    with open(HTACCESS_FILE) as f:
        return f.read()
