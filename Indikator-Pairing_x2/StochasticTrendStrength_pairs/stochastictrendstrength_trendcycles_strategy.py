import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und TrendCycles
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'TrendCycles': 1.0
        })
    )
