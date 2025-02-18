import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'ParabolicSAR': 1.0
        })
    )
