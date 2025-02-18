import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_WilliamsR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und WilliamsR
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'WilliamsR': 1.0
        })
    )
