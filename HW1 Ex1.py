c_pappa = 1.6
m_pappa = 1.8
n_pappa = 2.0
c_hcg = 30.5
m_hcg = 33.8
n_hcg = 35.1
c_cps = 60.8
m_cps = 64.4
n_cps = 67.2
c_cst = 1.2
m_cst = 1.4
n_cst = 1.1
print("1st trimester prenatal screening calculator")
name = str(input("Enter the patient's name: "))
age = int(input("Enter patient's age (full years): "))
if age >= 25:
        print("Alert! Increased age risk! ")
race = str(input("Enter the patient's race (C for Caucasian/M for Mongoloid/N for Negroid): "))
pappa = float(input("Enter the patient's PAPP-A test result: "))
hcg = float(input("Enter the patient's fbHCG test result: "))
cps = float(input("Enter the CPS: "))
cst = float(input("Enter the CST: "))
print(f"Data for risk calculation: PAPP-A - {pappa} mMe/ml; fbHCG - {hcg} ng/ml; CPS - {cps} mm; CST - {cst} mm")
if race == "C":
    mom_pappa = pappa / c_pappa
    mom_hcg = hcg / c_hcg
    mom_cps = cps / c_cps
    mom_cst = cst / c_cst
    mom_mediana = (mom_pappa + mom_hcg + mom_cps + m_cst) // 4
    if mom_mediana > 0:
        print("No risks")
    elif mom_mediana <= 0:
        print("Risks increased!!!")
    else:
            print("Error!")
elif race == "M":
    mom_pappa = pappa / m_pappa
    mom_hcg = hcg / m_hcg
    mom_cps = cps / m_cps
    mom_cst = cst / m_cst
    mom_mediana = (mom_pappa + mom_hcg + mom_cps + m_cst) // 4
    if mom_mediana > 0:
        print("No risks")
    elif mom_mediana <= 0:
        print("Risks increased!!!")
    else:
        print("Error!")
elif race == "N":
    mom_pappa = pappa / n_pappa
    mom_hcg = hcg / n_hcg
    mom_cps = cps / n_cps
    mom_cst = cst / n_cst
    mom_mediana = (mom_pappa + mom_hcg + mom_cps + m_cst) // 4
    if mom_mediana > 0:
        print("No risks")
    elif mom_mediana <= 0:
        print("Risks increased!!!")
    else:
        print("Error!")