__all__ = [
    "PLURALS",
    "ACCESS",
    "TOC",
    "COMMENTS_MODE",
    "IS_CREATOR",
    "LANGUAGE",
]

PLURALS = {
    "Event": "events",
    "Project": "projects",
    "Question": "questions",
    "Request": "requests",
    "Script": "scripts",
    "Thread": "threads",
    "Ware": "wares",
}

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
