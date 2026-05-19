class SemanticRolloutPredictor:
    def analyze_confidence(self, deployment_matrix):
        confidence_score = 99.8
        if deployment_matrix.get('eu-central') == 'drifting':
            confidence_score -= 15.0
        return confidence_score
