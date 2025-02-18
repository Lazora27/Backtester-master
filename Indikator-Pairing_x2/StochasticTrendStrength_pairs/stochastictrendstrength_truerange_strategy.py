import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und TrueRange
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'TrueRange': 1.0
        })
    )
