import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'HilbertTrendline': 1.0
        })
    )
