import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
