Django Pipeline Compass
=======================

django-pipeline-compass is a compiler for [django-pipeline](https://github.com/cyberdelia/django-pipeline). Making it really easy to use scss and compass with out requiring the compass gem.

To install it :

    pip install django-pipeline-compass

And add it as a compiler to pipeline in your django `settings.py`.

	PIPELINE_COMPILERS = (
 		'pipeline_compass.compiler.CompassCompiler',
	)

To suggest a feature or report a bug :
<https://github.com/vbabiy/django-pipeline-compass/issues>
