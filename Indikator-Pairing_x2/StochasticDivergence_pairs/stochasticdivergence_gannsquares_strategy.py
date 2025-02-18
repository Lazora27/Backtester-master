import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und GannSquares
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'GannSquares': 1.0
        })
    )
