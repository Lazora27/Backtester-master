import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HistoricalATR_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HistoricalATR und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'HistoricalATR': {
                'class': HistoricalATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalATR'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'HistoricalATR': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
