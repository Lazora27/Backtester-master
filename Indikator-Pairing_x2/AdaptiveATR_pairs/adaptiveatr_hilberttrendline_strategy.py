import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'HilbertTrendline': 1.0
        })
    )
