import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
