<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <title>Estimator</title>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="description" content="UI for Estimator">
    <meta name="keywords" content="COVID-19, Estimator">
    <meta name="author" content="Ezekiel Obhafuoso">

    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">

    <link rel="stylesheet" href="./static/styles.css" />
</head>

<body>
    <section class="page-header">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <div class="content">
                        <h1 class="page-name">Estimator</h1>
                        <nav aria-label="breadcrumb">
                            <ol class="breadcrumb">
                                <li class="breadcrumb-item"><a href="#">Home</a></li>
                                <li class="breadcrumb-item active" aria-current="page">Estimator</li>
                            </ol>
                        </nav>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section class="estimator-area section">
        <div class="container">
            <div class="row">
                <div class="col-md-8">
                    <div class="block">
                        <h4 class="widget-title">
                            User Input
                        </h4>
                        <form class="checkout-form" method='post'>

                            <label for="population">Population</label>
                            <input name="population" type="number" class="form-control"
                                placeholder="Population" data-population="population" required autofocus>

                            <label for="timeToElapse">Time to Elapse</label>
                            <input name="timeToElapse" type="number" class="form-control"
                                placeholder="Time To Elapse in Days" data-time-to-elapse="timeToElapse" required>

                            <label for="reportedCases">Number of Reported Cases</label>
                            <input name="reportedCases" type="number" class="form-control"
                                placeholder="Number of Reported Cases" data-reported-cases="reportedCases" required>

                            <label for="totalHospitalBeds">Total Number of Hosipital Beds</label>
                            <input name="totalHospitalBeds" type="number" class="form-control" placeholder="Total Number of Hospital Beds"
                                data-total-hospital-beds="totalHospitalBeds" required>

                            <p>Select Input Period Type:</p>
                            <input type="radio" data-period-type= "inputPeriodTypeDays" name="inputPeriodType" >
                            <label class="radioLabels" for="inputPeriodTypeDays">Days</label><br>
                            <input type="radio" data-period-type= "inputPeriodTypeDays" name="inputPeriodType">
                            <label class="radioLabels" for="age2">Weeks</label><br>
                            <input type="radio" data-period-type= "inputPeriodTypeDays" name="inputPeriodType">
                            <label class="radioLabels" for="age3">Months</label><br><br>

                            <button class="btn btn-lg btn-primary btn-block" data-go-
                            estimate= "estimate" type="submit"> Submit </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
        </div>
    </section>

    <footer class="footer section text-center">
        <div class="container">
            <div class="row">
                <div class="col-md-12">
                    <p class="copyright-text">Copyright &#9400;Created by Obhafuoso Ezekiel</p>
                </div>
            </div>
        </div>
    </footer>

    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
</body>

</html>