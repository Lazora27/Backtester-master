import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_LinearRegressionTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und LinearRegressionTrend
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'LinearRegressionTrend': {
                'class': LinearRegressionTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionTrend'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'LinearRegressionTrend': 1.0
        })
    )
