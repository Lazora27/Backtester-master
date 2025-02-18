import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
