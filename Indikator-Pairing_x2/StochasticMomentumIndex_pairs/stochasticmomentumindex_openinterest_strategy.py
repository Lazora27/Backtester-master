import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
