run_pipeline:
	python ml_pipeline/training.py
run_backend:
	PYTHONPATH=. python serverside/app.py
run_frontend:
	PYTHONPATH=. streamlit run clientside/app.py
