import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
