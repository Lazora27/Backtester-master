import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'WeeklyCycle': 1.0
        })
    )
