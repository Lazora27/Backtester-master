import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'HilbertTrendline': 1.0
        })
    )
