#!/usr/bin/env python
import warnings
from crew import Dinsdag

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    #DFG is the default plot
    focus = str(input("What is the focus of your research? e.g. bottlenecks, financial risks, IT and Cyber risks, audit risk"))
    company = str(input("What is the company your research? e.g. Google, IKEA, proctor and gamble (P&G)"))
    process = str(input("What is the process your research should analyse? e.g. loan application, purchase-to-pay, IT incident handling, order to cash"))
    filename = str(input("What is the filename (stored int he Event_logs folder) do you want to analyse? e.g. O2C.csv"))
    prompt_DK_company = f'Conduct a thorough research about {company}  using the context of {process} if you have it. Use the tavily_search_company and make sure that the research has many references.'
    prompt_DK_process = f'Conduct a thorough research about the {process} process using the context of {company} if you have it. Use the tavily_search_process and make sure that the research has many references.'
    inputs = {
        'process': process,
        'company': company,
        'focus': focus,
        'chosen_approach': 'DFG',
        'filename': filename,
        'prompt_DK_company': prompt_DK_company,
        'prompt_DK_process': prompt_DK_process,
        'skip_analysis': """ Answer: 
Based on the provided DFG model of the Order to Cash (O2C) process, here are the most important process steps/activities identified through the analysis:

### 1. **Order Validation**
   - **Frequency:** 54,646
   - **Performance:** 1,887,445.053
   - **Justification:** Order Validation has the highest frequency of occurrences, indicating it is a critical step in the process. It serves as a gatekeeper for subsequent activities, such as Customer Credit Check and Order Approval. High performance metrics suggest that while it is frequently executed, it may also be a potential bottleneck if delays occur here.

### 2. **Customer Credit Check**
   - **Frequency:** 43,544
   - **Performance:** 2,987,028.747
   - **Justification:** This step is crucial for assessing the financial viability of the customer before proceeding with the order. The high frequency and performance metrics indicate that it is a significant step that can impact the overall process flow. Additionally, the presence of loops (e.g., Customer Credit Check -> Customer Credit Check) suggests that there may be instances of rework or delays, which could lead to inefficiencies.

### 3. **Order Approval**
   - **Frequency:** 37,281
   - **Performance:** 525,194.681
   - **Justification:** Order Approval is a key decision point in the process. Its frequency indicates that it is a common step, and its performance metrics suggest that it may be a point where delays could occur, especially if there are dependencies on prior steps like Customer Credit Check. The connections to multiple subsequent steps highlight its importance in maintaining the flow of the process.

### 4. **Payment Received**
   - **Frequency:** 40,498
   - **Performance:** 1,635,238.573
   - **Justification:** Payment Received is a critical step that signifies the completion of the transaction. Its high frequency indicates that it is a common occurrence in the process, and it directly influences cash flow. The performance metrics suggest that while it is executed frequently, it may also be a point where delays can occur, especially if there are issues with invoicing or payment processing.

### 5. **Goods Shipped**
   - **Frequency:** 31,015
   - **Performance:** 1,639,812.259
   - **Justification:** Goods Shipped is a pivotal step in the fulfillment of customer orders. The frequency indicates that it is a common step in the process, and its performance metrics suggest that it is executed efficiently. However, it is also a critical point where delays can impact customer satisfaction and overall process efficiency, especially if there are issues with inventory or logistics.

These steps are essential for identifying potential bottlenecks and crucial events in the O2C process, allowing for targeted improvements to enhance overall efficiency and customer satisfaction.""",
        'skip_flow': """If I have a process with flow:

Order Received -> Order Validation ( frequency = 54646  performance = 1887445.053 )
Order Validation -> Customer Credit Check ( frequency = 43544  performance = 2987028.747 )
Payment Received -> Order Completed ( frequency = 40498  performance = 1635238.573 )
Order Approval -> Order Confirmation Sent ( frequency = 37281  performance = 525194.681 )
Prepare Goods for Shipment -> Goods Shipped ( frequency = 31015  performance = 1639812.259 )
Goods Shipped -> Send Invoice ( frequency = 30876  performance = 482145.317 )
Customer Credit Check -> Order Approval ( frequency = 29528  performance = 1434384.558 )
Send Invoice -> Payment Received ( frequency = 27028  performance = 2017517.642 )
Order Confirmation Sent -> Prepare Goods for Shipment ( frequency = 25519  performance = 2806987.813 )
Customer Credit Check -> Customer Credit Check ( frequency = 21514  performance = 1802303.237 )
Order Completed -> Order Received ( frequency = 19131  performance = 9426820.411 )
Goods Shipped -> Payment Received ( frequency = 18835  performance = 1026978.311 )
Order Confirmation Sent -> Order Approval ( frequency = 17787  performance = 887339.433 )
Prepare Goods for Shipment -> Send Invoice ( frequency = 17352  performance = 1589910.118 )
Send Invoice -> Goods Shipped ( frequency = 16931  performance = 1206892.969 )
Order Approval -> Prepare Goods for Shipment ( frequency = 14209  performance = 2414321.513 )
Customer Credit Check -> Order Confirmation Sent ( frequency = 14102  performance = 1840181.556 )
Order Validation -> Order Validation ( frequency = 9055  performance = 1778946.229 )
Customer Credit Check -> Order Rejected ( frequency = 8662  performance = 1750313.184 )
Order Completed -> Customer Credit Check ( frequency = 7946  performance = 4908076.197 )
Order Completed -> Order Validation ( frequency = 7351  performance = 3635440.639 )
Order Rejected -> Order Completed ( frequency = 7296  performance = 3122052.632 )
Payment Received -> Order Received ( frequency = 5881  performance = 3552933.474 )
Order Validation -> Order Approval ( frequency = 5063  performance = 2519391.029 )
Customer Credit Check -> Order Received ( frequency = 4520  performance = 3736188.186 )
Order Validation -> Order Completed ( frequency = 4263  performance = 1545234.806 )
Order Confirmation Sent -> Order Received ( frequency = 4236  performance = 5148882.450 )
Order Completed -> Prepare Goods for Shipment ( frequency = 3892  performance = 5811132.025 )
Order Received -> Order Completed ( frequency = 3470  performance = 2255622.813 )
Order Validation -> Prepare Goods for Shipment ( frequency = 3268  performance = 3179889.125 )
Prepare Goods for Shipment -> Order Received ( frequency = 3229  performance = 3309145.680 )
Order Validation -> Order Confirmation Sent ( frequency = 2927  performance = 2691470.940 )
Send Invoice -> Order Received ( frequency = 2805  performance = 2978041.476 )
Order Received -> Customer Credit Check ( frequency = 2792  performance = 2202538.775 )
Order Validation -> Order Received ( frequency = 2745  performance = 7164037.792 )
Goods Shipped -> Order Completed ( frequency = 2557  performance = 1014391.936 )
Order Completed -> Order Approval ( frequency = 2493  performance = 3034562.744 )
Goods Shipped -> Order Received ( frequency = 2346  performance = 5331288.440 )
Customer Credit Check -> Prepare Goods for Shipment ( frequency = 2239  performance = 2117470.210 )
Payment Received -> Goods Shipped ( frequency = 2156  performance = 1019608.163 )
Send Invoice -> Prepare Goods for Shipment ( frequency = 2069  performance = 1013665.346 )
Order Approval -> Order Received ( frequency = 2067  performance = 3875169.666 )
Order Completed -> Order Confirmation Sent ( frequency = 1772  performance = 3211544.526 )
Order Confirmation Sent -> Send Invoice ( frequency = 1748  performance = 2453631.281 )
Order Validation -> Payment Received ( frequency = 1497  performance = 1276415.230 )
Order Confirmation Sent -> Order Completed ( frequency = 1460  performance = 1517797.808 )
Prepare Goods for Shipment -> Payment Received ( frequency = 1379  performance = 1928610.326 )
Customer Credit Check -> Goods Shipped ( frequency = 1366  performance = 1517867.789 )
Order Received -> Prepare Goods for Shipment ( frequency = 1355  performance = 1744197.697 )
Order Confirmation Sent -> Goods Shipped ( frequency = 1248  performance = 1972748.269 )
Order Validation -> Goods Shipped ( frequency = 1222  performance = 1711278.363 )
Customer Credit Check -> Payment Received ( frequency = 1152  performance = 1396623.177 )
Order Confirmation Sent -> Payment Received ( frequency = 1136  performance = 1810463.239 )
Order Rejected -> Order Received ( frequency = 1085  performance = 4985558.710 )
Customer Credit Check -> Order Completed ( frequency = 1068  performance = 2028456.742 )
Order Completed -> Goods Shipped ( frequency = 1050  performance = 3878318.914 )
Payment Received -> Order Validation ( frequency = 1018  performance = 2837687.446 )
Payment Received -> Customer Credit Check ( frequency = 964  performance = 4548056.577 )
Send Invoice -> Order Validation ( frequency = 928  performance = 2726309.677 )
Order Approval -> Send Invoice ( frequency = 895  performance = 2146737.788 )
Order Completed -> Send Invoice ( frequency = 889  performance = 4079848.144 )
Customer Credit Check -> Send Invoice ( frequency = 841  performance = 1366896.885 )
Order Received -> Goods Shipped ( frequency = 803  performance = 1319862.516 )
Send Invoice -> Order Completed ( frequency = 799  performance = 971040.300 )
Prepare Goods for Shipment -> Order Completed ( frequency = 763  performance = 1230101.284 )
Prepare Goods for Shipment -> Order Validation ( frequency = 748  performance = 2829774.465 )
Order Received -> Send Invoice ( frequency = 727  performance = 1385688.033 )
Order Completed -> Payment Received ( frequency = 708  performance = 4173703.136 )
Order Approval -> Order Completed ( frequency = 695  performance = 1542583.424 )
Order Validation -> Order Rejected ( frequency = 685  performance = 4533540.438 )
Goods Shipped -> Order Validation ( frequency = 677  performance = 3199931.521 )
Order Received -> Payment Received ( frequency = 671  performance = 420166.498 )
Order Approval -> Goods Shipped ( frequency = 623  performance = 2025149.181 )
Order Validation -> Send Invoice ( frequency = 602  performance = 2429129.302 )
Order Received -> Order Approval ( frequency = 598  performance = 1539210.903 )
Goods Shipped -> Customer Credit Check ( frequency = 569  performance = 5177613.005 )
Order Approval -> Payment Received ( frequency = 562  performance = 1935680.605 )
Order Received -> Order Confirmation Sent ( frequency = 479  performance = 1571217.620 )
Order Received -> Order Rejected ( frequency = 315  performance = 3820251.429 )
Send Invoice -> Customer Credit Check ( frequency = 279  performance = 3563711.613 )
Order Completed -> Order Rejected ( frequency = 240  performance = 4044240.000 )
Goods Shipped -> Order Confirmation Sent ( frequency = 161  performance = 4706956.025 )
Goods Shipped -> Order Approval ( frequency = 160  performance = 4479060.000 )
Goods Shipped -> Prepare Goods for Shipment ( frequency = 137  performance = 7698806.715 )
Order Confirmation Sent -> Order Validation ( frequency = 129  performance = 2467447.907 )
Order Approval -> Order Validation ( frequency = 73  performance = 2385764.384 )
Prepare Goods for Shipment -> Customer Credit Check ( frequency = 24  performance = 2829300.000 )
_end of the flow_
"""
    }
    
    try:
        Dinsdag().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


run()
#
# def train():
#     """
#     Train the crew for a given number of iterations.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         'current_year': str(datetime.now().year)
#     }
#     try:
#         Dinsdag().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
#
#     except Exception as e:
#         raise Exception(f"An error occurred while training the crew: {e}")
#
# def replay():
#     """
#     Replay the crew execution from a specific task.
#     """
#     try:
#         Dinsdag().crew().replay(task_id=sys.argv[1])
#
#     except Exception as e:
#         raise Exception(f"An error occurred while replaying the crew: {e}")
#
# def test():
#     """
#     Test the crew execution and returns the results.
#     """
#     inputs = {
#         "topic": "AI LLMs",
#         "current_year": str(datetime.now().year)
#     }
#
#     try:
#         Dinsdag().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
#
#     except Exception as e:
#         raise Exception(f"An error occurred while testing the crew: {e}")
