import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_StochasticMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und StochasticMomentumIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'StochasticMomentumIndex': 1.0
        })
    )
