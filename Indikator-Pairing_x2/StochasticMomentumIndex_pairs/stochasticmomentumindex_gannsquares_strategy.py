import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_GannSquares_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und GannSquares
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'GannSquares': 1.0
        })
    )
