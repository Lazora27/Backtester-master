import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_CompositeIndexDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und CompositeIndexDivergence
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'CompositeIndexDivergence': 1.0
        })
    )
