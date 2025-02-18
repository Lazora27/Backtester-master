import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
