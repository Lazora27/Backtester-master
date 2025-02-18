import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_GannSquareReversal_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und GannSquareReversal
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'GannSquareReversal': 1.0
        })
    )
