# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)
loan_status=data['Loan_Status'].value_counts()
loan_status.plot(kind="bar")
plt.show()

#Code starts here


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv(path)
property_and_loan=data.groupby(["Property_Area","Loan_Status"]).size().unstack()
property_and_loan.plot(kind='bar', stacked=False,)
plt.xlabel("Property Area")
plt.ylabel('Loan Status')
plt.xlabel(90)
plt.show()


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv(path)
education_and_loan=data.groupby(["Education","Loan_Status"]).size().unstack()
education_and_loan.plot(kind='bar', stacked=True,)
plt.xlabel("Education Status")
plt.ylabel('Loan Status')
plt.xlabel(45)
plt.show()


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv(path)
graduate=data[data['Education'] == 'Graduate']
not_graduate=data[data['Education'] == 'Not Graduate']
graduate["LoanAmount"].plot(kind='density',label='Graduate')
not_graduate["LoanAmount"].plot(kind='density',label='Not Graduate')
plt.show()













#Code ends here

#For automatic legend display
plt.legend()


# --------------
#Code starts here
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(path)
fig,(ax_1,ax_2,ax_3)=plt.subplots(nrows = 3 , ncols = 1)
data.plot(x="ApplicantIncome",y="LoanAmount",kind="scatter",ax=ax_1)
ax_1.set_title("Applicant Income")

data.plot(x="CoapplicantIncome",y="LoanAmount",kind="scatter",ax=ax_2)
ax_2.set_title("Coapplicant Income")

data["TotalIncome"]=data["ApplicantIncome"]+data["CoapplicantIncome"]
data.head()
data.plot(x="TotalIncome",y="LoanAmount",kind="scatter",ax=ax_3)
ax_3.set_title("Total Income")
plt.show()



