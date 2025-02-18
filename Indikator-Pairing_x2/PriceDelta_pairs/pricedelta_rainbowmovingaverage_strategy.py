import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
