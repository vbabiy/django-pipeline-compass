Django Pipeline Compass
=======================

django-pipeline-compass is a compiler for [django-pipeline](https://github.com/cyberdelia/django-pipeline). Making it really easy to use scss and compass with out requiring the compass gem.

To install it :

    pip install django-pipeline-compass

And add it as a compiler to pipeline in your django `settings.py`.

	PIPELINE_COMPILERS = (
 		'pipeline_compass.compiler.CompassCompiler',
	)


To use image_sprites the following configuration must be added.
	SCSS_STATIC_ROOT = "/tmp/scss/css" 
	#point to any temporary directory, must end in /css for collectstatic command

	STATICFILES_DIRS = (
	        ...	
		SCSS_STATIC_ROOT+/../,
		#for collectstatic
		SCSS_STATIC_ROOT,
		#for running in debug mode
	)
This library supports a limited subset of the image_sprites functionality.  Please see pyscss documentation for more details.


This library relies upon pyscss, look there to see what commands are supported.
http://pyscss.readthedocs.org/en/latest/

To suggest a feature or report a bug :
<https://github.com/vbabiy/django-pipeline-compass/issues>
