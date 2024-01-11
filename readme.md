# Converts an EDL file exported from Resolve's timeline into Youtube chapters
- First marker needs to be at zero as Youtube needs that to know they're chapters
- Supports single markers of any colour, untested with those range markers

Pulls the EDL file from next to the script. Only supports one EDL file at a time

## To export markers from Resolve:
Right click the timeline in the media pool, go to Timelines > Export > Timeline markers to EDL...