import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'EaseOfMovement': 1.0
        })
    )
