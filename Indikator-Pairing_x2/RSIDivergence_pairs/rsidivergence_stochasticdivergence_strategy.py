import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_StochasticDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und StochasticDivergence
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'StochasticDivergence': 1.0
        })
    )
