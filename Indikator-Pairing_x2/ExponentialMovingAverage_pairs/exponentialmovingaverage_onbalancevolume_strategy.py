import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
