import backtrader as bt
from ..base_strategy import FlexibleStrategy

class LinearRegressionTrend_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von LinearRegressionTrend und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'LinearRegressionTrend': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
