import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'HilbertTrendline': 1.0
        })
    )
