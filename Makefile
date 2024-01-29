TARGET=container-cargo
BUILD_FLAGS=-y -F --log-level=WARN
PYTHONPATH=/usr/lib/python3.11/site-packages

all: build

build: clean
	PYTHONOPTIMIZE=2 pyinstaller --paths $(PYTHONPATH) src/main.py $(BUILD_FLAGS) -n $(TARGET)

install: build
	mv ./dist/${TARGET} /usr/local/bin
	mkdir -p /etc/${TARGET}
	touch config.ini /etc/${TARGET}

uninstall:
	rm -rf /usr/local/bin/$(TARGET)
	rm -rf /etc/${TARGET}

clean:
	rm -rf build
	rm -rf dist
	rm -rf $(TARGET).spec
