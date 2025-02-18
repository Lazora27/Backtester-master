import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
