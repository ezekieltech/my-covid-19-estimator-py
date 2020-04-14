def estimator(input):
    res = {
        "data": {},
        "impact": {},
        "severeImpact": {}
    }

    # challenge 1
    res["data"] = input
    res["impact"]["currentlyInfected"] = input["reportedCases"] * 10
    res["severeImpact"]["currentlyInfected"] = input["reportedCases"] * 50

    if input['periodType'] == "weeks":
        input['timeToElapse'] = input['timeToElapse'] * 7
    elif input["periodType"] == "months":
        input["timeToElapse"] = input["timeToElapse"] * 30

    factor = input["timeToElapse"] // 3

    effective_factor = 2 ** factor

    res["impact"]["infectionsByRequestedTime"] = res["impact"]["currentlyInfected"] * effective_factor
    res["severeImpact"]["infectionsByRequestedTime"] = res["severeImpact"]["currentlyInfected"] * effective_factor

    # Challenge 2
    res["impact"]["severeCasesByRequestedTime"] = int(
        res["impact"]["infectionsByRequestedTime"] * 0.15)
    res["severeImpact"]["severeCasesByRequestedTime"] = int(
        res["severeImpact"]["infectionsByRequestedTime"] * 0.15)

    beds_unused_by_hospital = input["totalHospitalBeds"] * 0.35
    res["impact"]["hospitalBedsByRequestedTime"] = int(beds_unused_by_hospital - \
        res["impact"]["severeCasesByRequestedTime"])
    res["severeImpact"]["hospitalBedsByRequestedTime"] = int(beds_unused_by_hospital - \
        res["severeImpact"]["severeCasesByRequestedTime"])

    # Challenge 3
    res["impact"]["casesForICUByRequestedTime"] = res["impact"]["infectionsByRequestedTime"] * 0.05
    res["severeImpact"]["casesForICUByRequestedTime"] = res["severeImpact"]["infectionsByRequestedTime"] * 0.05

    res["impact"]["casesForVentilatorsByRequestedTime"] = int(res["impact"]["infectionsByRequestedTime"] * 0.02)
    res["severeImpact"]["casesForVentilatorsByRequestedTime"] = int(res["severeImpact"]["infectionsByRequestedTime"] * 0.02)

    res["impact"]["dollarsInFlight"] = int((res["impact"]["infectionsByRequestedTime"]
                                        * 0.65) * input["region"]["avgDailyIncomeInUSD"]*input['timeToElapse'])
    res["severeImpact"]["dollarsInFlight"] = int((
        res["severeImpact"]["infectionsByRequestedTime"] * 0.65) * input["region"]["avgDailyIncomeInUSD"]*input['timeToElapse'])

    return res
