run:
	@poetry run python ./termOS.py

build:
		@poetry run pyinstaller --onefile --name termOS ./termOS.py

reset:
	@rm ./data/termOS.state
	@poetry run python ./termOS.py

clean:
	@rm -rf ./dist ./build ./__pycache__ *.spec
