import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
