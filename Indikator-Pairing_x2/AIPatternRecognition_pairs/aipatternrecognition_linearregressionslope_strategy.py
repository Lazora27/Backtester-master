import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
