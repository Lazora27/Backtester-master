import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
