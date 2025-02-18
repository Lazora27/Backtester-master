import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und SuperMACD
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'SuperMACD': 1.0
        })
    )
