import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'HilbertTrendline': 1.0
        })
    )
