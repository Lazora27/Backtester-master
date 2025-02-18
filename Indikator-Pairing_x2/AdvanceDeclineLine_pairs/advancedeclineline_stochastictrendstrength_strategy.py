import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
