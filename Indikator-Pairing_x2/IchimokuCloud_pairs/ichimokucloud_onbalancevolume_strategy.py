import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
