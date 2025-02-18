import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'AverageLogRange': 1.0
        })
    )
