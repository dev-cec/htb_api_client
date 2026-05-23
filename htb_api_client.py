import requests
from typing import Dict, Any, Optional, List
from pathlib import Path
import json


class HTBAPIClient:
    """Client for accessing HackTheBox API endpoints"""
    
    def __init__(self, api_key: str):
        """
        Initialize the HTB API client
        
        Args:
            api_key: The API key for authentication
        """
        self.base_url = "https://labs.hackthebox.com/api"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "User-Agent": "HTB-API-Client/1.0",
        })
    
    def _make_request(self, endpoint: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """
        Make a GET request to the API
        
        Args:
            endpoint: API endpoint (without base URL)
            params: Query parameters
            
        Returns:
            JSON response as dictionary
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, timeout=30)
        response.raise_for_status()
        return response.json()
    
    # University endpoints
    def get_universities(self, per_page: int = 15, page: int = 1) -> Dict[str, Any]:
        """
        Get list of universities
        
        Args:
            per_page: Number of universities per page
            page: Page number
            
        Returns:
            Dictionary containing universities data with pagination info
        """
        endpoint = "/v5/universities"
        params = {"per_page": per_page, "page": page}
        return self._make_request(endpoint, params)
    
    def get_my_university(self) -> Dict[str, Any]:
        """
        Get current user's university
        
        Returns:
            Dictionary containing university data
        """
        endpoint = "/v4/university/my"
        return self._make_request(endpoint)
    
    def get_university_profile(self, university_id: int) -> Dict[str, Any]:
        """
        Get university profile
        
        Args:
            university_id: ID of the university
            
        Returns:
            Dictionary containing university profile data
        """
        endpoint = f"/v4/university/profile/{university_id}"
        return self._make_request(endpoint)
    
    def get_university_stats(self, university_id: int) -> Dict[str, Any]:
        """
        Get university statistics
        
        Args:
            university_id: ID of the university
            
        Returns:
            Dictionary containing university stats
        """
        endpoint = f"/v5/universities/{university_id}/stats"
        return self._make_request(endpoint)
    
    def get_university_members(self, university_id: int) -> List[Dict[str, Any]]:
        """
        Get university members
        
        Args:
            university_id: ID of the university
            
        Returns:
            List of member dictionaries
        """
        endpoint = f"/v4/university/members/{university_id}"
        response = self._make_request(endpoint)
        # Based on the response, this returns a list directly
        return response if isinstance(response, list) else []
    
    def get_university_invitations(self, university_id: int) -> Dict[str, Any]:
        """
        Get university invitations
        
        Args:
            university_id: ID of the university
            
        Returns:
            Dictionary containing invitations data
        """
        endpoint = f"/v4/university/invitations/{university_id}"
        return self._make_request(endpoint)
    
    # User endpoints
    def get_user_basic_profile(self, user_id: int) -> Dict[str, Any]:
        """
        Get basic user profile
        
        Args:
            user_id: ID of the user
            
        Returns:
            Dictionary containing user profile data
        """
        endpoint = f"/v4/user/profile/basic/{user_id}"
        return self._make_request(endpoint)
    
    def get_user_experience(self, account_uuid: str) -> Dict[str, Any]:
        """
        Get user experience data
        
        Args:
            account_uuid: UUID of the account
            
        Returns:
            Dictionary containing experience data
        """
        endpoint = f"/experience/v1/account/{account_uuid}"
        return self._make_request(endpoint)
    
    def get_badges(self) -> Dict[str, Any]:
        """
        Get all badges
        
        Returns:
            Dictionary containing badges data
        """
        endpoint = "/v4/badges"
        return self._make_request(endpoint)
    
    def get_user_season_ranks(self, user_id: int) -> Dict[str, Any]:
        """
        Get user season ranks
        
        Args:
            user_id: ID of the user
            
        Returns:
            Dictionary containing season ranks data
        """
        endpoint = f"/v4/season/user/{user_id}/ranks"
        return self._make_request(endpoint)
    
    def get_user_progress(self, user_id: int, progress_type: str) -> Dict[str, Any]:
        """
        Get user progress for a specific type
        
        Args:
            user_id: ID of the user
            progress_type: Type of progress (machines, challenges, sherlocks, prolab, fortress)
            
        Returns:
            Dictionary containing progress data
        """
        endpoint = f"/v4/user/profile/progress/{progress_type}/{user_id}"
        return self._make_request(endpoint)
    
    def get_user_progress_chart(self, user_id: int, duration: str = "1M", content_type: str = "machines") -> Dict[str, Any]:
        """
        Get user progress chart data
        
        Args:
            user_id: ID of the user
            duration: Duration for chart (e.g., 1M for 1 month)
            content_type: Type of content (machines, challenges, etc.)
            
        Returns:
            Dictionary containing chart data
        """
        endpoint = f"/v4/users/{user_id}/profile/progress/chart"
        params = {"duration": duration, "content_type": content_type}
        return self._make_request(endpoint, params)
    
    def get_user_activity(self, user_id: int, per_page: int = 5) -> Dict[str, Any]:
        """
        Get user activity
        
        Args:
            user_id: ID of the user
            per_page: Number of activities per page
            
        Returns:
            Dictionary containing activity data
        """
        endpoint = f"/v5/user/profile/activity/{user_id}"
        params = {"per_page": per_page}
        return self._make_request(endpoint, params)
    
    def get_user_badges(self, user_id: int, rare: Optional[int] = None) -> Dict[str, Any]:
        """
        Get user badges
        
        Args:
            user_id: ID of the user
            rare: Filter by rarity level (optional)
            
        Returns:
            Dictionary containing user badges data
        """
        endpoint = f"/v4/user/profile/badges/{user_id}"
        params = {}
        if rare is not None:
            params["rare"] = rare
        return self._make_request(endpoint, params)
    
    def get_user_content_counts(self, user_id: int) -> Dict[str, Any]:
        """
        Get user content counts
        
        Args:
            user_id: ID of the user
            
        Returns:
            Dictionary containing content counts (machine, challenge, sherlock, writeup)
        """
        endpoint = f"/v5/user/profile/content/{user_id}/counts"
        return self._make_request(endpoint)
    
    # Utility method to load data from saved files (for testing)
    @staticmethod
    def load_from_file(filepath: str) -> Dict[str, Any]:
        """
        Load JSON data from a file
        
        Args:
            filepath: Path to the JSON file
            
        Returns:
            Dictionary containing the loaded data
        """
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)


# Example usage
if __name__ == "__main__":
    # This would normally come from environment variables
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    api_key = os.getenv("HTB_API_KEY", "")
    
    if not api_key:
        print("HTB_API_KEY not set in environment")
    else:
        client = HTBAPIClient(api_key)
        
        # Example: Get universities
        try:
            universities = client.get_universities()
            print(f"Found {len(universities.get('data', []))} universities")
            if universities.get('data'):
                print(f"First university: {universities['data'][0]['name']}")
        except Exception as e:
            print(f"Error: {e}")