import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
