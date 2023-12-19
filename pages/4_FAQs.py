import streamlit as st

st.set_page_config(page_title="faq")


def display_faq(question, answer):
    st.write(f"**Q: {question}**")
    st.write(f"A: {answer}")
    st.write("")

def main():

    st.markdown("<h1 style='text-decoration: underline; color:#2f72de; font-family: Georgia, serif; '>Real Estate FAQs</h1>", unsafe_allow_html=True)

    faqs = [
        ("How are property prices determined?", "Property prices are influenced by factors such as location, property size, amenities, market demand, and economic conditions."),
        ("What steps are involved in the home-buying process?", "The home-buying process typically involves pre-approval, property search, offer submission, inspection, mortgage approval, and closing."),
        ("How can I list my property for sale?", "You can list your property for sale by creating an account on our platform, providing property details, and following the guided listing process."),
        ("What are the differences between flats and houses?", "Flats are typically multi-unit buildings with shared spaces, while houses are standalone properties with private spaces. Prices vary based on size and location."),
        ("How can I find information about the safety of a neighborhood?", "Our app provides safety ratings and crime statistics for different neighborhoods to help you make informed decisions."),
        ("What are the current trends in the real estate market?", "Stay updated on market trends through our app, which offers insights into property pricing, demand, and emerging market hotspots."),
        ("What legal considerations should I be aware of when buying a property?", "Legal considerations include property title checks, zoning regulations, and understanding the terms of the sales contract."),
        ("How does the mortgage application process work?", "The mortgage application process involves submitting financial information, getting pre-approved, selecting a mortgage type, and finalizing the loan."),
        ("What are the responsibilities of a homeowner?", "Homeowners are responsible for property maintenance, paying property taxes, homeowners' association fees (if applicable), and complying with local regulations."),
        ("How do I use the features of the real estate app?", "Our app features user-friendly navigation. Explore home listings, use the price predictor, engage with the chatbot assistant, and access neighborhood insights."),
        ("Are there financing options available for homebuyers?",
         "Yes, there are various financing options available, including conventional loans, FHA loans, and VA loans. We can help you explore the best option based on your financial situation."),
        ("Can I negotiate the terms of my mortgage?",
         "Yes, you can negotiate the terms of your mortgage, including interest rates and closing costs. It's advisable to compare offers from different lenders to find the best deal."),
        ("What amenities are typically available in residential areas?",
         "Common amenities in residential areas include parks, schools, shopping centers, and healthcare facilities. Our app provides information on the amenities available in different neighborhoods."),
        ("How can I identify potential investment opportunities in real estate?",
         "Look for areas with growing demand, infrastructure developments, and positive economic indicators. Our app offers insights into market trends and potential investment hotspots."),
        ("Is there a guide for using the chatbot assistant?",
         "Yes, we provide a user-friendly guide within the app to help you make the most of the chatbot assistant. It can assist you with property recommendations, market trends, and general inquiries."),
        ("What types of mortgage options are available?",
         "Common mortgage options include fixed-rate mortgages, adjustable-rate mortgages (ARMs), and government-backed loans such as FHA and VA loans. Each option has its own features and considerations."),
        ("Can I get assistance with property-related queries through the app?",
         "Absolutely! Our chatbot assistant is designed to help you with property-related queries, neighborhood information, and general real estate guidance."),
        ("What is the response time for support requests?",
         "We strive to respond to support requests promptly. Our team is dedicated to providing assistance and ensuring a positive experience for our users."),
        ("How do I create an account on the app?",
         "Creating an account is easy. Simply click on the 'Sign Up' or 'Create Account' button, and follow the prompts to provide the necessary information."),
        ("What should I do if I forget my password?",
         "If you forget your password, use the 'Forgot Password' option on the login page. Follow the instructions to reset your password securely."),
        ("What are the benefits of getting pre-approved for a mortgage?",
         "Getting pre-approved for a mortgage gives you a clear understanding of your budget, strengthens your offer when buying a property, and streamlines the home-buying process."),
        ("Are there government programs for first-time homebuyers?",
         "Yes, there are government programs, such as FHA and VA loans, that offer benefits for first-time homebuyers. These programs often have lower down payment requirements."),
        ("How can I maintain my property to increase its value?",
         "Regular maintenance, landscaping, and home improvements can increase the value of your property. Focus on curb appeal, energy efficiency, and addressing any necessary repairs."),

    ]

    st.markdown("## Frequently Asked Questions")

    for q, a in faqs:
        display_faq(q, a)

if __name__ == "__main__":
    main()
