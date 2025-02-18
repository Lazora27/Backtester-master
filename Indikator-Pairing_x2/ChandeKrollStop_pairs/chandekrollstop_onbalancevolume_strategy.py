import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
