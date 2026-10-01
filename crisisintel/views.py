
import numpy as np
import pandas as pd
import plotly.express as px

from django.shortcuts import render
from django.contrib import messages

from .models import Prediction
from .services import model


# ==========================================
# DASHBOARD
# ==========================================
def dashboard(request):

    prediction = None
    confidence = None

    # Single Tweet Prediction
    if request.method == "POST":

        tweet = request.POST.get("tweet")

        if tweet:

            pred = model.predict([tweet])[0]

            probs = model.predict_proba([tweet])[0]

            confidence = round(
                np.max(probs) * 100,
                2
            )

            Prediction.objects.create(
                tweet=tweet,
                category=pred,
                confidence=confidence
            )

            prediction = pred

    # Recent Predictions
    history = Prediction.objects.order_by(
        "-created_at"
    )[:10]

    # Total Predictions
    total_predictions = Prediction.objects.count()

    # Analytics
    all_predictions = Prediction.objects.all()

    pie_chart = None
    bar_chart = None
    most_common = "No Data"

    if all_predictions.exists():

        df = pd.DataFrame(
            list(
                all_predictions.values(
                    "category"
                )
            )
        )

        counts = (
            df["category"]
            .value_counts()
            .reset_index()
        )

        counts.columns = [
            "category",
            "count"
        ]

        # Most Common Category
        most_common = counts.iloc[0]["category"]

        # Pie Chart
        pie = px.pie(
            counts,
            names="category",
            values="count",
            title="Prediction Distribution"
        )

        # Bar Chart
        bar = px.bar(
            counts,
            x="category",
            y="count",
            title="Category Count"
        )

        pie_chart = pie.to_html(
            full_html=False,
            include_plotlyjs="cdn"
        )

        bar_chart = bar.to_html(
            full_html=False,
            include_plotlyjs=False
        )

    context = {
        "prediction": prediction,
        "confidence": confidence,
        "history": history,
        "total_predictions": total_predictions,
        "most_common": most_common,
        "pie_chart": pie_chart,
        "bar_chart": bar_chart,
    }

    return render(
        request,
        "crisisintel/dashboard.html",
        context
    )


# ==========================================
# HISTORY PAGE
# ==========================================
def history_page(request):

    predictions = Prediction.objects.order_by(
        "-created_at"
    )

    context = {
        "predictions": predictions
    }

    return render(
        request,
        "crisisintel/history.html",
        context
    )


# ==========================================
# CSV UPLOAD PAGE
# ==========================================
def upload_csv(request):

    predictions = []

    if request.method == "POST":

        csv_file = request.FILES.get(
            "csv_file"
        )

        if not csv_file:

            messages.error(
                request,
                "Please upload a CSV file."
            )

        else:

            try:

                df = pd.read_csv(
                    csv_file
                )

                if "tweet" not in df.columns:

                    messages.error(
                        request,
                        "CSV must contain a column named 'tweet'."
                    )

                else:

                    for tweet in df["tweet"]:

                        if pd.isna(tweet):
                            continue

                        pred = model.predict(
                            [tweet]
                        )[0]

                        probs = model.predict_proba(
                            [tweet]
                        )[0]

                        confidence = round(
                            np.max(probs) * 100,
                            2
                        )

                        Prediction.objects.create(
                            tweet=tweet,
                            category=pred,
                            confidence=confidence
                        )

                        predictions.append(
                            {
                                "tweet": tweet,
                                "category": pred,
                                "confidence": confidence,
                            }
                        )

            except Exception as e:

                messages.error(
                    request,
                    f"Error: {str(e)}"
                )

    context = {
        "predictions": predictions
    }

    return render(
        request,
        "crisisintel/upload.html",
        context
    )

