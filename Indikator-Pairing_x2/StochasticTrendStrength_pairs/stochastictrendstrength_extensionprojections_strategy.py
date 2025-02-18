import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'ExtensionProjections': 1.0
        })
    )
