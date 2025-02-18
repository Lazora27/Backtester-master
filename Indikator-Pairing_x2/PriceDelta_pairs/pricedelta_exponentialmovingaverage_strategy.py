import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
