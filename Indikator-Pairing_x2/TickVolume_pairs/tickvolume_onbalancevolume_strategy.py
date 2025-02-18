import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
