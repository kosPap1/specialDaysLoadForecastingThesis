def GoodFridayHoliday():
    # Libraries imports

    from functions.dataInput import load2014, load2015, load2016, load2017, load2018, load2019, temp2014, \
        temp2015, temp2016, temp2017, temp2018, temp2019
    from functions.predictionEngine import predictionEngine1, predictionEngineCase2, predictionEngineCase3,\
        predictionEngineCase4
    import os

    # Holiday Datasets Lags

    # 10. Good Friday

    # Train Load lag inputs
    loadTrainDayTarget = load2016['2016-04-29']
    loadTrainDayMinus1 = load2016['2016-04-28']
    loadTrainDayMinus7 = load2016['2016-04-22']
    loadTrainDayMinus365 = load2015['2015-04-10']
    loadTrainDayMinus730 = load2014['2014-04-18']

    # Train temperature lag inputs
    temperTrainDayTarget = temp2016['2016-04-29']
    temperTrainDayMinus1 = temp2016['2016-04-28']
    temperTrainDayMinus7 = temp2016['2016-04-22']
    temperTrainDayMinus365 = temp2015['2015-04-10']
    temperTrainDayMinus730 = temp2014['2014-04-18']

    ##############################################
    # Test lag days input

    loadTestDayTarget = load2019['2019-04-26']
    loadTestDayMinus1 = load2019['2019-04-25']
    loadTestDayMinus7 = load2019['2019-04-19']
    loadTestDayMinus365 = load2018['2018-04-06']
    loadTestDayMinus730 = load2017['2017-04-14']

    # Train temperature lag inputs
    temperTestDayTarget = temp2019['2019-04-26']
    temperTestDayMinus1 = temp2019['2019-04-25']
    temperTestDayMinus7 = temp2019['2019-04-19']
    temperTestDayMinus365 = temp2018['2018-04-06']
    temperTestDayMinus730 = temp2017['2017-04-14']

    ########################################################################################################################

    filename = os.path.basename(__file__)
    # predictionEngine1(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
    #                  loadTestDayTarget, loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, filename)

    # # Case 2
    # predictionEngineCase2(loadTrainDayTarget, loadTrainDayMinus1, loadTrainDayMinus7, loadTrainDayMinus365,
    #                       loadTestDayTarget,
    #                       loadTestDayMinus1, loadTestDayMinus7, loadTestDayMinus365, filename)

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








