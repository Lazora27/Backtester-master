import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'SmoothedCycle': 1.0
        })
    )
