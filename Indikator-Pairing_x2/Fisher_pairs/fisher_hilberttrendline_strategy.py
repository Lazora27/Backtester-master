import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'HilbertTrendline': 1.0
        })
    )
