Instalar dependencias para ejecutar el Instalador Unificado de Plone ::
  # aptitude install gcc g++ make tar unzip bzip2 libssl-dev libxml2-dev zlib1g-dev libjpeg62-dev libreadline5-dev readline-common wv xpdf-utils
  # aptitude install subversion

Descargar el archivo de instalación unificada de Plone 3.3.5 ::
  # wget http://launchpad.net/plone/3.3/3.3.5/+download/Plone-3.3.5-UnifiedInstaller.tgz

Descomprimir el archivo de instalación ::
  # tar zxvf Plone-3.3.5-UnifiedInstaller.tgz

Acceder al directorio de instalación ::
  # cd Plone-3.3.5-UnifiedInstaller

Ejecutar instalación la instalación con un servidor monolítico ::
  # ./install.sh standalone

Acceder al directorio del servidor Zope ::
  # cd /usr/local/Plone/zinstance/

Descargar los archivos de configuración buildout para resconstruir el sitio PloneEdu ::
  # svn checkout http://plone-ve.googlecode.com/svn/trunk/PloneEduIUTE/ PloneEduIUTE

Acceda al directorio de configuración buildout ::
  $ cd PloneEduIUTE/

Ejecutar la construcción del sitio con Buildout ::
  $ ./bin/buildout -vNc 02-administration-03-Security.cfg

Iniciar el servidor en modo depuración ::
  $ ./bin/instance fg

Para cancelar el servidor presione la combinación de teclas crtl + d

Iniciar el servidor como un servido del sistema ::
  $ ./bin/instance start
