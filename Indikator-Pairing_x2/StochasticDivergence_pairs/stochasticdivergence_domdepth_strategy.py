import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_DOMDepth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und DOMDepth
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'DOMDepth': 1.0
        })
    )
