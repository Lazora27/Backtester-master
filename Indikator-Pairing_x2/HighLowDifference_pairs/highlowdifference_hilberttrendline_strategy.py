import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'HilbertTrendline': 1.0
        })
    )
