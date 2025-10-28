# Examination 4 - Install a Web Server

Now that we know how to install software on a machine through Ansible, we can
begin to look at how to set up a machine with services.

A typical use case is how to get a web server up and running, and coincidentally
we happen to have one of our hosts named `webserver`.

As in the previous examination, we can use the [ansible.builtin.package](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/package_module.html)
module to install the prerequisite software.

Create a new file, you can call it what you like, but in the example below, it's referred to as
`webserver.yml`.

    ---
    - name: Install a webserver
      hosts: web
      become: true
      tasks:
        - name: Ensure nginx is installed
          ansible.builtin.package:
            name: nginx
            state: latest

        - name: Ensure nginx is started at boot
          ansible.builtin.service:
            name: nginx
            enabled: true

The above is a playbook that will install [nginx](https://nginx.org/), a piece of software that can
act as a HTTP server, reverse proxy, content cache, load balancer, and more.

Now, we can run `curl` to see if web server does what we want it to (serve HTTP pages on TCP port 80):

    $ curl -v http://<IP ADDRESS OF THE WEBSERVER>

Change the text within '<' and '>' to the actual IP address of the web server. It may work with the
name of the server too, but this depends on how `libvirt` and DNS is set up on your machine.

Is the response what we expected?

    $ curl -v http://192.168.121.10
    *   Trying 192.168.121.10:80...
    * connect to 192.168.121.10 port 80 from 192.168.121.1 port 46036 failed: Connection refused
    * Failed to connect to 192.168.121.10 port 80 after 0 ms: Could not connect to server
    * closing connection #0
    curl: (7) Failed to connect to 192.168.121.10 port 80 after 0 ms: Could not connect to server

# QUESTION A

Refer to the documentation for the [ansible.builtin.service](https://docs.ansible.com/ansible/latest/collections/ansible/builtin/service_module.html)
module.

How can we make the web server start with an addition of just one line to the playbook above?

Svar:
enabled: true ser till att tjänsten startar vid boot.

# QUESTION B

You make have noted that the `become: true` statement has moved from a specific task to the beginning
of the playbook, and is on the same indentation level as `tasks:`.

What does this accomplish?

Svar:
När jag placerar "become: true" på samma indentation level som tasks: istället för inuti varje task betyder det att alla tasks i playbooken automatiskt körs som root, utan att behöva skriva become: true i varje task

- Tidigare behövde vi lägga become: true i varje enskild task som kräver root-rättigheter, t.ex. installation av paket eller start av tjänster.

- Genom att lägga det på playbook-nivå sparar vi tid, minskar risken för fel och gör playbooken mer läsbar.

- Varför det är viktigt: Många Ansible-uppgifter, som att installera program eller starta tjänster, kräver root-rättigheter. Genom att sätta det globalt säkerställer vi att alla tasks som behöver det får rätt behörighet direkt.

# QUESTION C

Copy the above playbook to a new playbook. Call it `04-uninstall-webserver.yml`.

Change the ordering of the two tasks. Make the web server stop, and disable it from starting at boot, and
make sure that `nginx` is uninstalled. Change the `name:` parameter of each task accordingly.

Run the new playbook, then make sure that the web server is not running (you can use `curl` for this), and
log in to the machine and make sure that there are no `nginx` processes running.

Why did we change the order of the tasks in the `04-uninstall-webserver.yml` playbook?

Svar:
Jag ändrade ordningen så att det först stoppar Nginx och stänger av autostart, innan den avinstalleras. 
Tar man bort Nginx först föröker tjänsten köras ändå vilket kan resultera i fel.
Ordningen Stoppa -> inaktivera -> avinstallera säkerställer att allt tas bort på ett säkert sätt. 

# BONUS QUESTION

Consider the output from the tasks above, and what we were actually doing on the machine.

What is a good naming convention for tasks? (What SHOULD we write in the `name:` field`?)

Svar:
Ett bra namn ska vara kort, tydligt och beskriva vad tasken gör.
om någon utomstående läser det ska dom snabbt förstå vad det handlar om.
Ska helst börja med ett verb.
Detta gör playbooken lättare att läsa och underhålla samt underlättar när man felsöker

