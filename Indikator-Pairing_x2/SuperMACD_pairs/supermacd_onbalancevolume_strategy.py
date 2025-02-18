import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
