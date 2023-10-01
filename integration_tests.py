#!/usr/bin/env python


import pytest
import time
from main import chain

known_colors = {
    'red', 'blue', 'yellow',  
    'green', 'orange', 'purple', 
}

@pytest.mark.integration
def test_chain_invoke():
    # Set maximum time (in seconds)
    max_allowed_time = 5  
    
    # Record the start time
    start_time = time.time()
    
    # Invoke the chain
    response = chain.invoke({"text": "colors"})
    
    # Record the end time
    end_time = time.time()
    
    # Calculate the duration
    duration = end_time - start_time
    
    # Assert that the response time is less than the maximum allowed time
    assert duration < max_allowed_time, f"API response took {duration} seconds, which is longer than the allowed {max_allowed_time} seconds"
    
    # Check if the API returns a list of colors:
    assert isinstance(response, list)
    assert len(response) == 5  # assuming API returns 5 colors

    # Assert that each color in the response is a known color
    for color in response:
        assert color in known_colors, f"Unknown color: {color}"
    
