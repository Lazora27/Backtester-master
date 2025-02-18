import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
