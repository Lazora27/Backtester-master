import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'HilbertTrendline': 1.0
        })
    )
