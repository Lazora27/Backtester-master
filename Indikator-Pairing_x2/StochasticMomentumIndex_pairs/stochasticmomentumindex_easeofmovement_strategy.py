import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'EaseOfMovement': 1.0
        })
    )
