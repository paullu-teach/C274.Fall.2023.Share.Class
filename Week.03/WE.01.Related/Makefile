test:
	python3 testwe1.py
	python3 passwordvalidate.py

testall:
	python3 alltestwe1.py

push:
	git commit -a
	git push
	@echo "***"
	@echo "*** Do a fresh clone (and testall) of the repo to ensure correctness ***"
	@echo "***"

clean:
# For MacOS
	-rm .DS_Store
	-rm -r __pycache__
