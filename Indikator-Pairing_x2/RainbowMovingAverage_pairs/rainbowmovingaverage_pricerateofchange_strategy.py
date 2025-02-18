import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
