import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'EaseOfMovement': 1.0
        })
    )
