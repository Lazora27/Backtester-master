import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
