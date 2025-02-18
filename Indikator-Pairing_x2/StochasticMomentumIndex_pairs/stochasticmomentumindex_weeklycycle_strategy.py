import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'WeeklyCycle': 1.0
        })
    )
