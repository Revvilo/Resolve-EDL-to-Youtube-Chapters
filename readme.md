# Converts an EDL file exported from Resolve's timeline into Youtube chapters
First marker needs to be at zero else you'll need to add your own to the chapters
Not tested with anything other than Resolve's single blue markers
Abuses pythons array slicing so the slicing is hard coded and not dynamic

Pulls the EDL file from next to the script. Only supports one EDL file at a time