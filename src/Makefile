run:
	@poetry run python3 ./termOS.py

build:
		@poetry run pyinstaller --onefile --name termOS ./termOS.py

reset:
	@rm ./data/termOS.state
	@poetry run python3 ./termOS.py

clean:
	@rm -rf ./dist ./build ./__pycache__ *.spec
