def estimator(input):
    res = {
        "data": {},
        "impact": {},
        "severeImpact": {}
    }

    res["data"] = input
    res["impact"]["currentlyInfected"] = input["reportedCases"] * 10
    res["severeImpact"]["currentlyInfected"] = input["reportedCases"] * 50

    res["impact"]["infectionsByRequestedTime"] = res["impact"]["currentlyInfected"] * 1024
    res["severeImpact"]["infectionsByRequestedTime"] = res["severeImpact"]["currentlyInfected"] * 1024

    res["impact"]["severeCasesByRequestedTime"] = res["impact"]["infectionsByRequestedTime"] * 0.15
    res["severeImpact"]["severeCasesByRequestedTime"] = res["severeImpact"]["infectionsByRequestedTime"] * 0.15

    beds_unused_by_hospital = input["totalHospitalBeds"] * .90 * 0.35
    res["impact"]["hospitalBedsByRequestedTime"] = beds_unused_by_hospital - \
        res["impact"]["severeCasesByRequestedTime"]
    res["severeImpact"]["hospitalBedsByRequestedTime"] = beds_unused_by_hospital - \
        res["severeImpact"]["severeCasesByRequestedTime"]

    res["impact"]["casesForICUByRequestedTime"] = res["impact"]["infectionsByRequestedTime"] * 0.05
    res["severeImpact"]["casesForICUByRequestedTime"] = res["severeImpact"]["infectionsByRequestedTime"] * 0.05

    res["impact"]["casesForVentilatorsByRequestedTime"] = res["impact"]["infectionsByRequestedTime"] * 0.05
    res["severeImpact"]["casesForVentilatorsByRequestedTime"] = res["severeImpact"]["infectionsByRequestedTime"] * 0.05

    if input['periodType'] == "weeks":
        input['timeToElapse'] = input['timeToElapse'] * 7
    elif input["periodType"] == "months":
        input["timeToElapse"] = input["timeToElapse"] * 30

    res["impact"]["dollarsInFlight"] = (res["impact"]["infectionsByRequestedTime"]
                                        * 0.65) * input["region"]["avgDailyIncomeInUSD"]*input['timeToElapse']
    res["severeImpact"]["dollarsInFlight"] = (
        res["severeImpact"]["infectionsByRequestedTime"] * 0.65) * input["region"]["avgDailyIncomeInUSD"]*input['timeToElapse']

    return res
