import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SharpeRatioIndicator_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SharpeRatioIndicator und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'SharpeRatioIndicator': {
                'class': SharpeRatioIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SharpeRatioIndicator'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'SharpeRatioIndicator': 1.0,
            'HilbertSinewave': 1.0
        })
    )
