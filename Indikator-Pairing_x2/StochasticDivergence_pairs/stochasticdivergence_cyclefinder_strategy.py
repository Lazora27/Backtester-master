import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und CycleFinder
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'CycleFinder': 1.0
        })
    )
