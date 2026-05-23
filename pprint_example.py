"""
Example usage of HTBAPIClient with pretty printing of JSON responses
This demonstrates how to fetch data from ALL HTB API endpoints in the HTBAPIClient class
and display it nicely with pprint
"""
import os
from pprint import pprint
from dotenv import load_dotenv
from htb_api_client import HTBAPIClient

def main():
    # Load environment variables
    load_dotenv()
    api_key = os.getenv("HTB_API_KEY", "")
    
    if not api_key:
        print("HTB_API_KEY not set in environment")
        return
    
    # Initialize the client
    client = HTBAPIClient(api_key)
    
    # Constants for API parameters
    UNIVERSITY_ID = 1
    USER_ID = 36994
    ACCOUNT_UUID = "9b1ecfdd-f537-48c0-b33b-e52f41ad0801"
    BADGE_RARITY_FILTER = 8
    PROGRESS_CHART_DURATION = "1M"
    PROGRESS_CHART_CONTENT_TYPE = "machines"
    ACTIVITY_COUNT = 3
    UNIVERSITIES_PER_PAGE = 3
    
    print("HTBAPIClient Complete Coverage with Pretty Printing")
    print("=" * 60)
    print("Demonstrating ALL methods from HTBAPIClient class\n")
    
    # Helper function to safely print with pprint
    def safe_pprint(label, data, max_items=None):
        print(f"\n{label}:")
        print("-" * (len(label) + 1))
        if isinstance(data, dict) and max_items:
            # Limit dict items for brevity
            limited_data = dict(list(data.items())[:max_items])
            pprint(limited_data)
            if len(data) > max_items:
                print(f"  ... and {len(data) - max_items} more items")
        else:
            pprint(data)
    
    # 1. get_universities
    try:
        universities_data = client.get_universities(per_page=UNIVERSITIES_PER_PAGE)
        safe_pprint(f"1. get_universities() - First {UNIVERSITIES_PER_PAGE} universities", universities_data)
    except Exception as e:
        print(f"1. get_universities() Error: {e}")
    
    # 2. get_my_university
    try:
        my_uni_data = client.get_my_university()
        safe_pprint("2. get_my_university()", my_uni_data)
    except Exception as e:
        print(f"2. get_my_university() Error: {e}")
    
    # 3. get_university_profile
    try:
        uni_profile_data = client.get_university_profile(UNIVERSITY_ID)
        safe_pprint(f"3. get_university_profile({UNIVERSITY_ID})", uni_profile_data)
    except Exception as e:
        print(f"3. get_university_profile({UNIVERSITY_ID}) Error: {e}")
    
    # 4. get_university_stats
    try:
        uni_stats_data = client.get_university_stats(UNIVERSITY_ID)
        safe_pprint(f"4. get_university_stats({UNIVERSITY_ID})", uni_stats_data)
    except Exception as e:
        print(f"4. get_university_stats({UNIVERSITY_ID}) Error: {e}")
    
    # 5. get_university_members
    try:
        uni_members_data = client.get_university_members(UNIVERSITY_ID)
        safe_pprint(f"5. get_university_members({UNIVERSITY_ID}) - Member list", uni_members_data)
    except Exception as e:
        print(f"5. get_university_members({UNIVERSITY_ID}) Error: {e}")
    
    # 6. get_university_invitations
    try:
        uni_invitations_data = client.get_university_invitations(UNIVERSITY_ID)
        safe_pprint(f"6. get_university_invitations({UNIVERSITY_ID})", uni_invitations_data)
    except Exception as e:
        print(f"6. get_university_invitations({UNIVERSITY_ID}) Error: {e}")
    
    # 7. get_user_basic_profile
    try:
        user_profile_data = client.get_user_basic_profile(USER_ID)
        safe_pprint(f"7. get_user_basic_profile({USER_ID})", user_profile_data)
    except Exception as e:
        print(f"7. get_user_basic_profile({USER_ID}) Error: {e}")
    
    # 8. get_user_experience
    try:
        user_exp_data = client.get_user_experience(ACCOUNT_UUID)
        safe_pprint("8. get_user_experience()", user_exp_data)
    except Exception as e:
        print(f"8. get_user_experience() Error: {e}")
    
    # 9. get_badges
    try:
        badges_data = client.get_badges()
        # Show summary to avoid huge output
        if isinstance(badges_data, dict) and 'categories' in badges_data:
            summary = {
                'total_categories': len(badges_data['categories']),
                'first_category': badges_data['categories'][0] if badges_data['categories'] else None
            }
            safe_pprint("9. get_badges() - Summary", summary)
        else:
            safe_pprint("9. get_badges()", badges_data)
    except Exception as e:
        print(f"9. get_badges() Error: {e}")
    
    # 10. get_user_season_ranks
    try:
        user_ranks_data = client.get_user_season_ranks(USER_ID)
        safe_pprint(f"10. get_user_season_ranks({USER_ID})", user_ranks_data)
    except Exception as e:
        print(f"10. get_user_season_ranks({USER_ID}) Error: {e}")
    
    # 11. get_user_progress - machines
    try:
        user_machines_data = client.get_user_progress(USER_ID, "machines")
        safe_pprint(f"11. get_user_progress({USER_ID}, 'machines')", user_machines_data)
    except Exception as e:
        print(f"11. get_user_progress({USER_ID}, 'machines') Error: {e}")
    
    # 11b. get_user_progress - challenges
    try:
        user_challenges_data = client.get_user_progress(USER_ID, "challenges")
        safe_pprint(f"11b. get_user_progress({USER_ID}, 'challenges')", user_challenges_data)
    except Exception as e:
        print(f"11b. get_user_progress({USER_ID}, 'challenges') Error: {e}")
    
    # 11c. get_user_progress - sherlocks
    try:
        user_sherlocks_data = client.get_user_progress(USER_ID, "sherlocks")
        safe_pprint(f"11c. get_user_progress({USER_ID}, 'sherlocks')", user_sherlocks_data)
    except Exception as e:
        print(f"11c. get_user_progress({USER_ID}, 'sherlocks') Error: {e}")
    
    # 11d. get_user_progress - prolab
    try:
        user_prolab_data = client.get_user_progress(USER_ID, "prolab")
        safe_pprint(f"11d. get_user_progress({USER_ID}, 'prolab')", user_prolab_data)
    except Exception as e:
        print(f"11d. get_user_progress({USER_ID}, 'prolab') Error: {e}")
    
    # 11e. get_user_progress - fortress
    try:
        user_fortress_data = client.get_user_progress(USER_ID, "fortress")
        safe_pprint(f"11e. get_user_progress({USER_ID}, 'fortress')", user_fortress_data)
    except Exception as e:
        print(f"11e. get_user_progress({USER_ID}, 'fortress') Error: {e}")
    
    # 12. get_user_progress_chart
    try:
        user_chart_data = client.get_user_progress_chart(USER_ID, PROGRESS_CHART_DURATION, PROGRESS_CHART_CONTENT_TYPE)
        safe_pprint(f"12. get_user_progress_chart({USER_ID}, '{PROGRESS_CHART_DURATION}', '{PROGRESS_CHART_CONTENT_TYPE}')", user_chart_data)
    except Exception as e:
        print(f"12. get_user_progress_chart({USER_ID}, '{PROGRESS_CHART_DURATION}', '{PROGRESS_CHART_CONTENT_TYPE}') Error: {e}")
    
    # 13. get_user_activity
    try:
        user_activity_data = client.get_user_activity(USER_ID, ACTIVITY_COUNT)
        safe_pprint(f"13. get_user_activity({USER_ID}, {ACTIVITY_COUNT})", user_activity_data)
    except Exception as e:
        print(f"13. get_user_activity({USER_ID}, {ACTIVITY_COUNT}) Error: {e}")
    
    # 14. get_user_badges
    try:
        user_badges_data = client.get_user_badges(USER_ID, BADGE_RARITY_FILTER)
        safe_pprint(f"14. get_user_badges({USER_ID}, {BADGE_RARITY_FILTER})", user_badges_data)
    except Exception as e:
        print(f"14. get_user_badges({USER_ID}, {BADGE_RARITY_FILTER}) Error: {e}")
    
    # 15. get_user_content_counts
    try:
        user_counts_data = client.get_user_content_counts(USER_ID)
        safe_pprint(f"15. get_user_content_counts({USER_ID})", user_counts_data)
    except Exception as e:
        print(f"15. get_user_content_counts({USER_ID}) Error: {e}")
    
    print("\n" + "=" * 60)
    print("All HTBAPIClient methods demonstrated with pprint!")
    print("=" * 60)

if __name__ == "__main__":
    main()