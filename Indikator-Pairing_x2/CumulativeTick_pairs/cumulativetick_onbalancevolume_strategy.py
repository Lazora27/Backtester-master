import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
