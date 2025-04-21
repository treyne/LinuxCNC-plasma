# Keep your post GUI customisations here to prevent them from being overwritten
# by updates or pncconf/stepconf changes.

# As an example:
# You currently have a plasmac:thc-enable signal which connects the
# plasmac_run.thc-enable-out output to the plasmac.thc-enable input.

# You want to connect the thc-enable pin of the plasmac component to a switch
# on your machine rather than let it be controlled from the GUI Run tab.

# First disconnect the GUI Run tab from the plasmac:thc-enable signal:
# unlinkp plasmac_run.thc.enable-out

# Then connect the plasmac:thc-enable signal to your switch:
# net plasmac:thc-enable your.switch-pin
