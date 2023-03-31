from marvin import ai_fn, Bot

@ai_fn
def product_manager_background_context():
    """
    Generate a job description for a product manager in the form of a bio.
    """

def product_team(n_members):
    """
    Generate a team of product managers.
    """
    return [Bot(personality=product_manager_background_context()) for _ in range(n_members)]
