def PredictionRevolutionAnniversary():
    # Prediction for Revolution Anniversary

    # Libraries imports
    from functions.dataInput import load2013, load2014, load2015, load2016, load2017, load2018, load2019, temp2013, \
        temp2014, temp2015, temp2016, temp2017, temp2018, temp2019
    from functions.predictionEngine import predictionEngine1, predictionEngineCase2, predictionEngineCase3, \
        predictionEngineCase4
    import os

    # Holiday Datasets Lags

    # 2. 25th March anniversary

    # Train lag days input
    loadTrainDayTarget = load2016['2016-03-25']
    loadTrainDayMinus1 = load2016['2016-03-24']
    loadTrainDayMinus7 = load2016['2016-03-18']
    loadTrainDayMinus365 = load2015['2015-03-25']
    loadTrainDayMinus730 = load2014['2014-03-25']

    # Train temperature lag inputs
    temperTrainDayTarget = temp2016['2016-03-25']
    temperTrainDayMinus1 = temp2016['2016-03-24']
    temperTrainDayMinus7 = temp2016['2016-03-18']
    temperTrainDayMinus365 = temp2015['2015-03-25']
    temperTrainDayMinus730 = temp2014['2014-03-25']

    ##############################################

    # Test lag days input
    loadTestDayTarget = load2019['2019-03-25']
    loadTestDayMinus1 = load2019['2019-03-24']
    loadTestDayMinus7 = load2018['2018-03-18']
    loadTestDayMinus365 = load2018['2018-03-25']
    loadTestDayMinus730 = load2017['2017-03-25']

    # Test lag temperature input
    temperTestDayTarget = load2019['2019-03-25']
    temperTestDayMinus1 = temp2019['2019-03-24']
    temperTestDayMinus7 = temp2018['2018-12-18']
    temperTestDayMinus365 = temp2018['2018-03-25']
    temperTestDayMinus730 = temp2017['2017-03-25']

    #######################################################################################################################
    filename = os.path.basename(__file__)
    # predictionEngine1(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
    #                  loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, filename)

    # Case 2
    # predictionEngineCase2(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
    #                       loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, filename)

    # Case 3
    # predictionEngineCase3(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
    #                       loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365,
    #                       temperTrainDayTarget, temperTrainDayMinus1, temperTrainDayMinus7, temperTrainDayMinus365,
    #                       temperTestDayTarget, temperTestDayMinus1, temperTestDayMinus7, temperTestDayMinus365,
    #                       filename)

    # Case 4

    predictionEngineCase4(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
                          loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365,
                          temperTrainDayTarget, temperTrainDayMinus1, temperTrainDayMinus7, temperTrainDayMinus365,
                          temperTestDayTarget, temperTestDayMinus1, temperTestDayMinus7, temperTestDayMinus365,
                          filename)






