import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
