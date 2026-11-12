import logging

import azure.functions as func

from prediction import make_prediction

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)


@app.route(route="predict")
def predict(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    tenure = req.params.get("tenure")
    monthly = req.params.get("monthly")
    techsupport = req.params.get("techsupport")

    if tenure and monthly and techsupport:
        prediction = make_prediction(
            tenure=float(tenure),
            MonthlyCharges=float(monthly),
            TechSupport_yes=float(techsupport),
        )
        return func.HttpResponse(
            f"Hello, the prediction that this customer will churn is: {prediction:.1%}"
        )
    else:
        return func.HttpResponse(
            "This HTTP triggered function executed successfully. Pass the tenure, monthly and techsupport values in the query string or in the request body for a valid response.",
            status_code=200,
        )
