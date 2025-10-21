# Examination 1 - Understanding SSH and public key authentication

Connect to one of the virtual lab machines through SSH, i.e.

    $ ssh -i deploy_key -l deploy webserver

Study the `.ssh` folder in the home directory of the `deploy` user:

    $ ls -ld ~/.ssh

Look at the contents of the `~/.ssh` directory:

    $ ls -la ~/.ssh/

## QUESTION A

What are the permissions of the `~/.ssh` directory?
drwx------ 700. Endast användaren kan läsa skriva och gå in i katalogen

Why are the permissions set in such a way?
katalogen innehåller privata nycklar och authorized_keys så den ska skyddas för att förhindra att obehöriga får åtkomst

## QUESTION B

What does the file `~/.ssh/authorized_keys` contain?
filen innehåller publika SSH nycklar som tillåter inloggning utan lösenord för användararen deploy

## QUESTION C

When logged into one of the VMs, how can you connect to the
other VM without a password?
genom SSH nyckel-par. kopiera webbservens publika nyckel till DB serven. Då kan deploy logga in direkt.

### Hints:

* man ssh-keygen(1)
* ssh-copy-id(1) or use a text editor

## BONUS QUESTION

Can you run a command on a remote host via SSH? How?
Ja, ssh deploy@dbserver "hostname"
kommandot kör hostname på dbserven som deploy och visar resulterar i webbserver-terminalen utan att logga in interaktivt. 
