def classify_pseudo_naive_bayes_line(inLine):
    # Ugly use of global variables, should be fully OO
    global PNBPosCount,PNBNegCount,PNBPosFeaturesCount,PNBNegFeaturesCount
    global TP,FP,TN,FN
    global TargetLabel
    global ForcedOnlyPos,ForcedOnlyNeg,NBDecide

    label = inLine.split()[0]
    featureList = inLine.split()[1:]

    # Compute priors, based on number of training instances
    TotalInstances = PNBPosCount + PNBNegCount
    pos_prior = float(PNBPosCount) / TotalInstances
    neg_prior = float(PNBNegCount) / TotalInstances

    # Compute likelihoods, based on conditional probabilities by features

    # ***** Positive case
    pos_likelihood = 1.0
    for w in featureList:
        if w in PNBPosFeatures:
            # cp is the ratio/contribution feature to a POSITIVE classification
            cp = (float(PNBPosFeatures[w])/ float(PNBPosFeaturesCount))
            log_cp = math.log(cp)
            pos_likelihood *= cp

    # Numerator of Bayes theorem (thus X)
    pos_posteriorX = pos_prior * pos_likelihood
    assert( pos_posteriorX > 0.0 )

    # ***** Negative case
    neg_likelihood = 1.0
    for w in featureList:
        if w in PNBNegFeatures:
            # cp is the ratio/contribution feature to a NEGATIVE classification
            cp = (float(PNBNegFeatures[w])/ float(PNBNegFeaturesCount))
            log_cp = math.log(cp)
            neg_likelihood *= cp

    # Numerator of Bayes theorem (thus X)
    neg_posteriorX = neg_prior * neg_likelihood
    assert( neg_posteriorX > 0.0 )

    # Make the prediction
    if (pos_posteriorX >= neg_posteriorX):
        predClass = TargetLabel[0]
    else:
        predClass = "Neg"

    if (pos_posteriorX != 0.0 and neg_posteriorX != 0.0):
        NBDecide += 1

    # Do the metrics
    delta = pos_posteriorX - neg_posteriorX     # Delta
    if predClass in TargetLabel:
        if predClass == label:
            TP += 1
        else:
            FP += 1
    else:
        if label not in TargetLabel:
            TN += 1
        else:
            FN += 1

    return((predClass,pos_posteriorX,neg_posteriorX))
