import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
