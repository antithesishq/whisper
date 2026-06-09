.PHONY: config whisper down run push

config:
	podman build config/ -t us-central1-docker.pkg.dev/molten-verve-216720/honey-pwhale-repository/antithesis-whisper-config:latest

whisper:
	podman build . -t us-central1-docker.pkg.dev/molten-verve-216720/honey-pwhale-repository/antithesis-whisper:latest

down:
	docker-compose -f config/docker-compose.yaml down -v

run: down
	docker-compose -f config/docker-compose.yaml up

.ONESHELL:
push: config whisper
	cd ~/src/customer/customer-honey-whale
	customer credentials_shell -c " \
	podman push us-central1-docker.pkg.dev/molten-verve-216720/honey-pwhale-repository/antithesis-whisper-config:latest \
	podman push us-central1-docker.pkg.dev/molten-verve-216720/honey-pwhale-repository/antithesis-whisper:latest"