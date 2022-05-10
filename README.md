# request

APPLICATION:
Genropy's Package for send REST requests inside yours Genropy Projects.
Useful to debug your API directly inside your genropy WebApp.

TO INSTALL:

Edit instanceconfig.py

	<packages>
    .. others packages
		<request pkgcode="request:request"/>
	</packages>

Edit menu.py

root.branch('Requests', pkg='request')
