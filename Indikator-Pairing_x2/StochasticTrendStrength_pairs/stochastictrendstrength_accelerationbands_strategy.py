import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'AccelerationBands': 1.0
        })
    )
