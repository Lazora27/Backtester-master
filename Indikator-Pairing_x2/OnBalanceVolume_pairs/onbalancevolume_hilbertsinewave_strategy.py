import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OnBalanceVolume_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OnBalanceVolume und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'OnBalanceVolume': 1.0,
            'HilbertSinewave': 1.0
        })
    )
