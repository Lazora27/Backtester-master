import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'HilbertTrendline': 1.0
        })
    )
