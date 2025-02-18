import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
