import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'HilbertTrendline': 1.0
        })
    )
