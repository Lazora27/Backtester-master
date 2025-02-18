import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_WilliamsAccumulationDistribution_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und WilliamsAccumulationDistribution
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'WilliamsAccumulationDistribution': {
                'class': WilliamsAccumulationDistribution,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsAccumulationDistribution'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'WilliamsAccumulationDistribution': 1.0
        })
    )
