# PyDIGGS
This repository will eventually contain Python tools for working with the Data Interchange for Geotechnical and Geoenvironmental Specialists ([DIGGS](https://geoinstitute.org/special-projects/diggs)) format.

This is currently just a simple proof of concept that extracts the name of a boring from a DIGGS file and writes it to a PDF. Along the way, it uses a Jinja template to render the name as HTML in memory.

This code only works in 64-bit Windows, as the repository includes a binary file of [wkhtmltopdf](https://wkhtmltopdf.org/) that's compiled for that environment. It also includes a sample XML file from [diggs-examples](https://github.com/DIGGSml/diggs-examples) plus the [diggs-schema](https://github.com/DIGGSml/diggs-schema) files, though I'm not using the schema files yet.