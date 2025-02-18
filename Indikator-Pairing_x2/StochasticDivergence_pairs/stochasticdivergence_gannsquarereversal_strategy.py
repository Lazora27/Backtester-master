import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'GannSquareReversal': 1.0
        })
    )
