from Main import Main

if __name__ == "__main__":
    filepath = r"C:\Users\modes\Documents\VScode\Python\IA\Trabalho_1_Modesto_Pereira_Lima_Verde_Neto\ConsumoCo2.csv"
    features = ['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB']
    target = 'CO2EMISSIONS'
    
    main_process = Main(filepath, features, target)
    
    main_process.run()