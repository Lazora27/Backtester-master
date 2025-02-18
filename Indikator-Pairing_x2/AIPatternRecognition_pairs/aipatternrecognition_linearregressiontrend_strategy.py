import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
