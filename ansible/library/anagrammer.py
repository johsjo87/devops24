#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        message=dict(type='str', required=True)
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    msg = module.params['message']
    reversed_msg = msg[::-1]

    # Fail if message is 'fail me'
    if msg == 'fail me':
        module.fail_json(msg='You requested this to fail',
                         original_message=msg,
                         reversed_message=reversed_msg,
                         changed=True)

    # Determine changed
    changed = msg != reversed_msg

    module.exit_json(
        changed=changed,
        original_message=msg,
        reversed_message=reversed_msg
    )

def main():
    run_module()

if __name__ == '__main__':
    main()
