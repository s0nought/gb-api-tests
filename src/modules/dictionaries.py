ACCESS = {
    "Public": "0",  # Everyone can access
    "Private": "2", # Only you, permit holders, studio leaders and moderators can access
}

TOC = {
    "Enabled": "true", # A Table Of Contents is automatically generated
    "Disabled": "false",
}

COMMENTS_MODE = {
    "Open": "open",       # Anyone can comment (except members you block or block you)
    "Buddies": "buddies", # Only you and your buddies can comment
    "Authors": "creator", # Only you, credited members and this Submission's studio members can comment (if studio release)
    "Locked": "locked",   # Commenting not allowed, but existing comments appear
    "Hidden": "hidden",   # Commenting not allowed and any existing comments are hidden
}

# "d" is generated; looks like it needs to be parsed from the injected script tag
# IMAGE_UPLOADER_D = { # Deja Vu
#     "Event": "8264696bb6dfbd487a98236ec3c724c9",
#     "Mod": "e36b3626ab232d1ce51ae9d79dfded05"
# }

IS_CREATOR = {
    "Yes": "true",
    "No": "false", # submitting it on behalf of the author(s)
}

LANGUAGE = {
    "CFG/dot": "cfg",
    "CSS": "css",
    "Gettext": "gettext",
    "HTML": "html5",
    "Javascript/JSON": "javascript",
    "Plain Text": "text",
    "XML": "xml",
    "YAML": "yaml",
}