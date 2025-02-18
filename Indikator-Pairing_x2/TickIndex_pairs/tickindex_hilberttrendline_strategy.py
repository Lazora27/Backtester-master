import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
