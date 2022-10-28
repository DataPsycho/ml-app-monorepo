run_pipeline:
	python ml/training.py
run_backend:
	PYTHONPATH=. python serverside/app.py
run_frontend:
	PYTHONPATH=. streamlit run clientside/app.py
run_test_client:
	PYTHONPATH=. python clientside/client.py
