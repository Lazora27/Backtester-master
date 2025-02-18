import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'WeeklyCycle': 1.0
        })
    )
