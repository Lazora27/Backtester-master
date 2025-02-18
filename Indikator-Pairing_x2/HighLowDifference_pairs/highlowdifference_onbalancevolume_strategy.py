import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
