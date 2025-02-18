import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und CycleFinder
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'CycleFinder': 1.0
        })
    )
