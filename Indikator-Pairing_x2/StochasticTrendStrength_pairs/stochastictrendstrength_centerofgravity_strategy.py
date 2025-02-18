import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'CenterOfGravity': 1.0
        })
    )
