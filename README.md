# Ansible Requirements

This is a simple package to iterate over the [Ansible Modules](https://docs.ansible.com/ansible/latest/modules/list_of_all_modules.html) all modules page. It will print each found "requirement" to stdout. The ultimate intention of this module is to allow you to quick determine the requirements across a set of modules you intend to use for your Ansible Playbooks.

# Roadmap

## 1.0 - Release Date - TBD

- Given a set of modules to review (all by default), output a sorted and unique list of requirements
- The process should be able to be called via the command line or via a service API
- Once a list of required modules is found an Ansible Playbook can be created to ensure those modules are present on the target system(s)
- Interface with the [ansible-playbook](https://github.com/acmeframework/ansible_playbook) Docker image to create an image with the appropriate Ansible host module requirements (mostly for Network Modules)
- others yet to be determined...

NOTE: Please excuse the Python code. I have traditionally programmed in other languages but felt Python is a better match for the Ansible community.
