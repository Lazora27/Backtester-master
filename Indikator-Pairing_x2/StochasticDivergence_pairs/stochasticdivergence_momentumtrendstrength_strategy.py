import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
