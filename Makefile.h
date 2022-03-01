# Load .env file variables into Makefile environment

# Convert .env-file to makefile format and export all variables
# to be accessible within make and shell commands
# Variable precedence order:
#   1) Environment variables
#   2) .env.local
#   3) .env
$(shell rm -f /tmp/.make_env)
ifneq ("$(wildcard .env.local)","")
	output := $(shell sed "s/=/ ?= /" .env.local > /tmp/.make_env)
endif
ifneq ("$(wildcard .env)","")
	output := $(shell sed "s/=/ ?= /" .env >> /tmp/.make_env)
endif

# Export variables from merged .env files
ifneq ("$(wildcard /tmp/.make_env)","")
	include /tmp/.make_env
	export
endif
