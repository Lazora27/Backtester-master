import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
