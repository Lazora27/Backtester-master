import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
