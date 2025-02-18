import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
