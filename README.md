Certbot Filecopy Installer
===

This is a certbot plugin designed to install certificates by copying the file contents rather than just symlinks.

Useful for systems that create or deploy certbot certificates across execution boundaries like containers.

Usage
--

`certbot --installer filecopy-installer --filecopy-installer-destination /path/to/your/desired/directory -d example.com .... your other certbot authentication and configuration options`
