Joomla 1.5 Appliance - Cutting Edge Content Management
======================================================

`Joomla!`_ is an award-winning Content Management System (CMS) for
building websites as well as a Model-view-controller (MVC) Web
Application Development framework. The system includes features such as
page caching to improve performance, RSS feeds, printable versions of
pages, news flashes, blogs, polls, website searching, and language
internationalization.

A separate appliance is available for the newer `Joomla 2.5 version`_.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Joomla 1.5 configurations:
   
   - Installed from upstream source code to /var/www/joomla
   - SEO optimization enabled by default.

- SSL support out of the box.
- Postfix MTA (bound to localhost) to allow sending of email
  (e.g., password recovery, user registration).
- `PHPMyAdmin`_ administration frontend for MySQL (listening on port
  12322 - uses SSL).
- Webmin modules for configuring Apache2, PHP and MySQL.

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, SSH, MySQL, and phpMyAdmin: username **root**
-  Joomla: username **admin**


.. _Joomla!: http://www.joomla.org/
.. _Joomla 2.5 version: http://www.turnkeylinux.org/joomla
.. _TurnKey Core: http://www.turnkeylinux.org/core
.. _PHPMyAdmin: http://www.phpmyadmin.net
