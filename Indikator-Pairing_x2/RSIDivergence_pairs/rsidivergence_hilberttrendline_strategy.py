import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'HilbertTrendline': 1.0
        })
    )
