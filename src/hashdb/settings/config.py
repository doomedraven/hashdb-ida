PLUGIN_SETTINGS = {
    "API_URL":         "https://hashdb.openanalysis.net",  # local, global
    "ENUM_PREFIX":     "hashdb_strings",                   # local, global
    "REQUEST_TIMEOUT": 15,    # in seconds                 # local, global
    "ALGORITHM":       None,  # algorithm name             # local
    "ALGORITHM_SIZE":  0,     # algorithm size             # local
}
# Note: hotkeys are bound to actions!
PLUGIN_HOTKEYS = {
    "lookup_hash":    "Alt+`",
    "hunt_hash_algo": None,
    "scan_hashes":    None
}

# TODO (printup): move these TODOs to git issues :)

# TODO (printup): the default API_URL should be modifiable by the user
#                 the user should have an option to be able to set it,
#                 at which point the API_URL would be saved in a global
#                 config file (IDA directory, or appdata (system support
#                 funkiness)?
# TODO (printup): the same applies for the ENUM_PREFIX and REQUEST_TIMEOUT
# TODO (printup): all of these variables should also be savable locally,
#                 which would be the preferred way (higher priority) of
#                 fetching user settings