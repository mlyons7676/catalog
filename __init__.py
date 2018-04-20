Last login: Fri Apr 20 12:59:02 on ttys000
Martins-MBP:~ martinlyons$ cd ~/.ssh/udacity_key.rsa
-bash: cd: /Users/martinlyons/.ssh/udacity_key.rsa: Not a directory
Martins-MBP:~ martinlyons$ ssh keygen -f ~/.ssh/udacity_key.rsa
ssh: Could not resolve hostname keygen: nodename nor servname provided, or not known
Martins-MBP:~ martinlyons$ ssh-keygen -f ~/.ssh/udacity_key.rsa
Generating public/private rsa key pair.
/Users/martinlyons/.ssh/udacity_key.rsa already exists.
Overwrite (y/n)? n
Martins-MBP:~ martinlyons$ cd /Users/martinlyons/.ssh/udacity_key.rsa
-bash: cd: /Users/martinlyons/.ssh/udacity_key.rsa: Not a directory
Martins-MBP:~ martinlyons$ cd /Users/martinlyons/.ssh/
Martins-MBP:.ssh martinlyons$ nano udacity_key.rsa
Martins-MBP:.ssh martinlyons$ cat ~/.ssh/udacity_key.rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDetxCfcaUt4NjYQyZiP9U4wWbzkedpQAD8jmXjla3XWSQQeeXrsu552rQHqjkhDiiwhVBYJ8OVcXJkygwmN3HTjn6QgDLKL/tF0Pl4ykKsV7laNjfn8+nZzebagxqaxT0RFM3kUDcAryyijKMusIgbPoqi4bop7GwHHd5m/CKWZ8ogrqZxkb0+EamoFlZNHpPiZ5CVFnb7TK4AhnWWSALeZ6/Us4ouAQ4BEhp7QBL5yaTncZPNrPNtz0d7m/IkLm4z+lHDFBwTLBL4k1HpconfcJJ7Kt9UQ19qtbsiacw9FGT4zm+6YqQF3+w9hXZKqbBe5T8FI7LYuzxytCDc/ZAz martinlyons@Martins-MBP.attlocal.net
Martins-MBP:.ssh martinlyons$ ssh -i ~/.ssh/udacity_key.rsa grader@13.58.109.116
The authenticity of host '13.58.109.116 (13.58.109.116)' can't be established.
ECDSA key fingerprint is SHA256:U67B/ZmwMN81tvglHOhoFfekokmARhpIR5J6tRC+ye4.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '13.58.109.116' (ECDSA) to the list of known hosts.
grader@13.58.109.116: Permission denied (publickey).
Martins-MBP:.ssh martinlyons$ ssh -i ~/.ssh/udacity_key.rsa grader@13.59.228.162 -p 2200
Enter passphrase for key '/Users/martinlyons/.ssh/udacity_key.rsa': 
Welcome to Ubuntu 16.04.4 LTS (GNU/Linux 4.4.0-1013-aws x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  Get cloud support with Ubuntu Advantage Cloud Guest:
    http://www.ubuntu.com/business/services/cloud

10 packages can be updated.
8 updates are security updates.


*** System restart required ***
Last login: Wed Apr 18 22:08:07 2018 from 108.220.125.195
grader@ip-172-26-9-55:~$ sudo nano /etc/ssh/sshd_config
[sudo] password for grader: 


























grader@ip-172-26-9-55:~$ sudo nano /etc/ssh/sshd_config
grader@ip-172-26-9-55:~$ sudo a2enmod wsgi
Module wsgi already enabled
grader@ip-172-26-9-55:~$ sudo service apache2 start
grader@ip-172-26-9-55:~$ sudo chown -R grader:grader catalog
chown: cannot access 'catalog': No such file or directory
grader@ip-172-26-9-55:~$ cd/var/www/catalog
-bash: cd/var/www/catalog: No such file or directory
grader@ip-172-26-9-55:~$ cd /var/www/catalog
grader@ip-172-26-9-55:/var/www/catalog$ sudo chown -R grader:grader catalog
grader@ip-172-26-9-55:/var/www/catalog$ cd catalog
grader@ip-172-26-9-55:/var/www/catalog/catalog$ ls
app.wsgi  catalog.wsgi  client_secrets.json  database_setup.py  database_setup.pyc  __init__.py  item.db  lotsofitems.py  README.md  venv
grader@ip-172-26-9-55:/var/www/catalog/catalog$ nano database_setup.py
grader@ip-172-26-9-55:/var/www/catalog/catalog$ nano __init__.py

  GNU nano 2.5.3                                  File: __init__.py                                                                           

    else:
        shops = session.query(Shop).all()
        return render_template('add.html', shops=shops, log_staus=log_staus)


# Edit item inforamtion in the shop
@app.route('/shop/<string:shop_name>/<int:item_id>/edit',
           methods=['GET', 'POST'])
def edit_item(item_id, shop_name):
    # login status check
    if 'username' in login_session:
        log_staus = "Logout"
    else:
        return redirect("/login")
    item = session.query(Item).filter_by(id=item_id).one()
    shops = session.query(Shop).all()
    if request.method == "POST":
        item.title = request.form["title"]
        item.price = request.form["price"]
        item.brand = request.form["brand"]
        item.price = request.form["discount_price"]
        item.shop_id = request.form["shop"]
        session.add(item)
        session.commit()
        flash("The item has been edited!")
        return redirect(url_for("shop_items", shop_name=shop_name))
    else:
        return render_template("edit.html", item=item, shop_name=shop_name,
                               log_staus=log_staus, shops=shops)


# Delete item in the shop
@app.route("/shop/<string:shop_name>/<int:item_id>/delete",
           methods=['GET', 'POST'])
def delete_item(item_id, shop_name):
    if 'username' in login_session:
        log_staus = "Logout"
    else:
        return redirect("/login")
    item = session.query(Item).filter_by(id=item_id).one()
    if request.method == "POST":
        session.delete(item)
        session.commit()
        flash("The item has been deleted!")
        return redirect(url_for("all_list"))
    else:
        return render_template("delete.html", item=item, shop_name=shop_name,
                               log_staus=log_staus)


if __name__ == '__main__':
    app.secret_key = "super_secret_key"
    app.debug = True
    app.run()
