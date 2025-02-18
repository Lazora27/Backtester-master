import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und CycleFinder
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'CycleFinder': 1.0
        })
    )
