def fillTensor(tensor):
    ##weekdays
    ##ageRange = [(0-4),(5-19),(20-29),(30-63),(64-120)]
    ##time
    ##building_type =[cafe, church,hospital, kindergarten, school,shop,sport,university,work,self.address]
    for wd in [0, 1, 2, 3, 4, 5, 6]:
        for age in [0, 1, 2, 3, 4]:
            for time in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]:
                for building_type in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    prob_value = 0
                    if 0 <= wd <= 4:
                        if age == 0:
                            if 10 <= time < 17:
                                if building_type == 0:
                                    prob_value = 0.01
                                elif building_type == 3:
                                    prob_value = 0.3
                                elif building_type == 5:
                                    prob_value = 0.05
                                elif building_type == 9:
                                    prob_value = 0.64
                                else:
                                    prob_value = 0
                            elif 17 <= time < 21:
                                if building_type == 0:
                                    prob_value = 0.1
                                elif building_type == 1:
                                    prob_value = 0.0025
                                elif building_type == 5:
                                    prob_value = 0.1
                                elif building_type == 6:
                                    prob_value = 0.0025
                                elif building_type == 9:
                                    prob_value = 0.795
                                else:
                                    prob_value = 0
                            else:
                                if building_type == 9:
                                    prob_value = 1
                                else:
                                    prob_value = 0
                        elif age == 1:
                            if 8 <= time < 15:
                                if building_type == 0:
                                    prob_value = 0.02
                                elif building_type == 4:
                                    prob_value = 0.9
                                elif building_type == 6:
                                    prob_value = 0.0025
                                elif building_type == 9:
                                    prob_value = 0.0775
                                else:
                                    prob_value = 0
                            elif 15 <= time < 22:
                                if building_type == 0:
                                    prob_value = 0.05
                                elif building_type == 1:
                                    prob_value = 0.0025
                                elif building_type == 5:
                                    prob_value = 0.2
                                elif building_type == 6:
                                    prob_value = 0.0025
                                elif building_type == 9:
                                    prob_value = 0.745
                                else:
                                    prob_value = 0
                            else:
                                if building_type == 5:
                                    prob_value = 0.005
                                elif building_type == 9:
                                    prob_value = 0.995
                                else:
                                    prob_value = 0
                        elif age == 2:
                            if 9 <= time < 16:
                                if building_type == 0:
                                    prob_value = 0.05
                                elif building_type == 1:
                                    prob_value = 0.0025
                                elif building_type == 5:
                                    prob_value = 0.1
                                elif building_type == 6:
                                    prob_value = 0.0025
                                elif building_type == 7:
                                    prob_value = 0.55
                                elif building_type == 8:
                                    prob_value = 0.1075
                                elif building_type == 9:
                                    prob_value = 0.1875
                                else:
                                    prob_value = 0
                            elif 16 <= time < 20:
                                if building_type == 0:
                                    prob_value = 0.2
                                elif building_type == 5:
                                    prob_value = 0.2
                                elif building_type == 6:
                                    prob_value = 0.0025
                                elif building_type == 7:
                                    prob_value = 0.1
                                elif building_type == 8:
                                    prob_value = 0.25
                                elif building_type == 9:
                                    prob_value = 0.2475
                                else:
                                    prob_value = 0
                            elif time >= 20 or time < 1:
                                if building_type == 0:
                                    prob_value = 0.15
                                elif building_type == 5:
                                    prob_value = 0.2
                                elif building_type == 6:
                                    prob_value = 0.0025
                                elif building_type == 8:
                                    prob_value = 0.04
                                elif building_type == 9:
                                    prob_value = 0.6075
                                else:
                                    prob_value = 0
                            else:
                                if building_type == 0:
                                    prob_value = 0.005
                                elif building_type == 8:
                                    prob_value = 0.05
                                elif building_type == 9:
                                    prob_value = 0.945
                                else:
                                    prob_value = 0
                        elif age == 3:
                            if 9 <= time <= 18:
                                if building_type == 0:
                                    prob_value = 0.04
                                elif building_type == 1:
                                    prob_value = 0.00125
                                elif building_type == 5:
                                    prob_value = 0.15
                                elif building_type == 8:
                                    prob_value = 0.70375
                                elif building_type == 9:
                                    prob_value = 0.105
                                else:
                                    prob_value = 0
                            elif time > 18 or time <= 1:
                                if building_type == 0:
                                    prob_value = 0.15
                                elif building_type == 5:
                                    prob_value = 0.2
                                elif building_type == 6:
                                    prob_value = 0.0025
                                elif building_type == 8:
                                    prob_value = 0.102
                                elif building_type == 9:
                                    prob_value = 0.5425
                                else:
                                    prob_value = 0
                            else:
                                if building_type == 0:
                                    prob_value = 0.01
                                elif building_type == 8:
                                    prob_value = 0.075
                                elif building_type == 9:
                                    prob_value = 0.915
                                else:
                                    prob_value = 0
                        else:
                            if 8 <= time <= 16:
                                if building_type == 0:
                                    prob_value = 0.05
                                elif building_type == 1:
                                    prob_value = 0.025
                                elif building_type == 5:
                                    prob_value = 0.2
                                elif building_type == 9:
                                    prob_value = 0.725
                                else:
                                    prob_value = 0
                            elif 16 <= time <= 21:
                                if building_type == 0:
                                    prob_value = 0.05
                                elif building_type == 5:
                                    prob_value = 0.1
                                elif building_type == 9:
                                    prob_value = 0.85
                                else:
                                    prob_value = 0
                            else:
                                if building_type == 9:
                                    prob_value = 1
                                else:
                                    prob_value = 0
                    else:
                        if age == 0:
                            if 10 <= time < 17:
                                if building_type == 0:
                                    prob_value = 0.15
                                elif building_type == 1:
                                    prob_value = 0.01
                                elif building_type == 5:
                                    prob_value = 0.15
                                elif building_type == 9:
                                    prob_value = 0.69
                                else:
                                    prob_value = 0
                            elif 17 <= time < 21:
                                if building_type == 0:
                                    prob_value = 0.15
                                elif building_type == 1:
                                    prob_value = 0.01
                                elif building_type == 5:
                                    prob_value = 0.2
                                elif building_type == 6:
                                    prob_value = 0.0025
                                elif building_type == 9:
                                    prob_value = 0.6375
                                else:
                                    prob_value = 0
                            else:
                                if building_type == 9:
                                    prob_value = 1
                                else:
                                    prob_value = 0
                        elif age == 1:
                            if 12 <= time < 18:
                                if building_type == 0:
                                    prob_value = 0.1
                                elif building_type == 5:
                                    prob_value = 0.0975
                                elif building_type == 6:
                                    prob_value = 0.0025
                                elif building_type == 9:
                                    prob_value = 0.8
                                else:
                                    prob_value = 0
                            elif 18 <= time < 22:
                                if building_type == 0:
                                    prob_value = 0.1
                                elif building_type == 5:
                                    prob_value = 0.2
                                elif building_type == 6:
                                    prob_value = 0.0025
                                elif building_type == 9:
                                    prob_value = 0.6975
                                else:
                                    prob_value = 0
                            else:
                                if building_type == 5:
                                    prob_value = 0.002
                                elif building_type == 9:
                                    prob_value = 0.998
                                else:
                                    prob_value = 0
                        elif age == 2:
                            if 12 <= time < 22:
                                if building_type == 0:
                                    prob_value = 0.2
                                elif building_type == 1:
                                    prob_value = 0.02
                                elif building_type == 5:
                                    prob_value = 0.25
                                elif building_type == 6:
                                    prob_value = 0.025
                                elif building_type == 8:
                                    prob_value = 0.05
                                elif building_type == 9:
                                    prob_value = 0.455
                                else:
                                    prob_value = 0
                            elif 22 <= time or time < 2:
                                if building_type == 0:
                                    prob_value = 0.1
                                elif building_type == 8:
                                    prob_value = 0.001
                                elif building_type == 9:
                                    prob_value = 0.899
                                else:
                                    prob_value = 0
                            else:
                                if building_type == 9:
                                    prob_value = 1
                                else:
                                    prob_value = 0
                        elif age == 3:
                            if 11 <= time <= 20:
                                if building_type == 0:
                                    prob_value = 0.1
                                elif building_type == 1:
                                    prob_value = 0.01
                                elif building_type == 5:
                                    prob_value = 0.2
                                elif building_type == 8:
                                    prob_value = 0.05
                                elif building_type == 9:
                                    prob_value = 0.64
                                else:
                                    prob_value = 0
                            elif time > 20 or time <= 2:
                                if building_type == 0:
                                    prob_value = 0.1
                                elif building_type == 5:
                                    prob_value = 0.15
                                elif building_type == 6:
                                    prob_value = 0.0025
                                elif building_type == 8:
                                    prob_value = 0.02
                                elif building_type == 9:
                                    prob_value = 0.7275
                                else:
                                    prob_value = 0
                            else:
                                if building_type == 8:
                                    prob_value = 0.007
                                elif building_type == 9:
                                    prob_value = 0.993
                                else:
                                    prob_value = 0
                        else:
                            if 8 <= time <= 16:
                                if building_type == 0:
                                    prob_value = 0.2
                                elif building_type == 1:
                                    prob_value = 0.05
                                elif building_type == 5:
                                    prob_value = 0.25
                                elif building_type == 9:
                                    prob_value = 0.54
                                else:
                                    prob_value = 0
                            elif 16 <= time <= 21:
                                if building_type == 0:
                                    prob_value = 0.05
                                elif building_type == 5:
                                    prob_value = 0.05
                                elif building_type == 9:
                                    prob_value = 0.9
                                else:
                                    prob_value = 0
                            else:
                                if building_type == 9:
                                    prob_value = 1
                                else:
                                    prob_value = 0

                    tensor[wd, age, time, building_type] = prob_value
