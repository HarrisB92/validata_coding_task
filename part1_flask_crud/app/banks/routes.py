from . import banks_bp

@banks_bp.get("/")
def list_banks():
    # Placeholder: will be implemented after DB layer is in place
    return {"message": "TODO: list banks"}
