import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
