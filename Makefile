TARGET=container-cargo
BUILD_FLAGS=-y -F --log-level=WARN

all: build

build: clean
	PYTHONOPTIMIZE=2 pyinstaller src/main.py $(BUILD_FLAGS) -n $(TARGET)

install: build
	sudo mv ./dist/${TARGET} /usr/local/bin
	sudo mkdir -p /etc/${TARGET}
	sudo cp config.ini /etc/${TARGET}

uninstall:
	sudo rm -rf /usr/local/bin/$(TARGET)
	sudo rm -rf /etc/${TARGET}

clean:
	rm -rf build
	rm -rf dist
	rm -rf $(TARGET).spec
