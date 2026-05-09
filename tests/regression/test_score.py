from src.core.score import compute_score


def test_score_bounds():
    score = compute_score(
        missing=0,
        outliers=0,
        schema_issues=0
    )

    assert 0 <= score <= 100
