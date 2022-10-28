curl -X curl http://127.0.0.1:5000/healthcheck/

curl -X POST curl http://127.0.0.1:5000/predict/ \
   -H 'Content-Type: application/json' \
   -d '{"Alcohol": 12.17, "Malic": 1.45, "Ash": 2.53, "Alcalinity": 19.0, "Magnesium": 104.0, "Phenols": 1.89, "Flavanoids": 1.75, "Nonflavanoids": 0.45, "Proanthocyanins": 1.03, "Color": 2.95, "Hue": 1.45, "Dilution": 2.23, "Proline": 355.0}'