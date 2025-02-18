import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
