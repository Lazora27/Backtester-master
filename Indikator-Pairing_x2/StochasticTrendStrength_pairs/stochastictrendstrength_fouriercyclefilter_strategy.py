import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
