import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_LinearRegressionSlope_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und LinearRegressionSlope
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'LinearRegressionSlope': {
                'class': LinearRegressionSlope,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LinearRegressionSlope'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'LinearRegressionSlope': 1.0
        })
    )
