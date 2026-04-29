from loaders import load_data
from validators import run_validations
from ai_explainer import generate_ai_explanation


print("Loading data...")
df=load_data()


print("Running validations...")
df=run_validations(df)


print("Generating AI explanations...")

ai_explanations=[]

for _,row in df.iterrows():

    explanation=generate_ai_explanation(
       row
    )

    ai_explanations.append(
       explanation
    )


df["AI_Explanation"]=ai_explanations


df.to_csv(
  "../output/billing_audit.csv",
  index=False
)

print(
 "Audit completed successfully."
)