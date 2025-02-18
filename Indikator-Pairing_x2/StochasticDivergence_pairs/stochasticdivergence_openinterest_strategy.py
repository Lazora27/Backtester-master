import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und OpenInterest
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'OpenInterest': 1.0
        })
    )
