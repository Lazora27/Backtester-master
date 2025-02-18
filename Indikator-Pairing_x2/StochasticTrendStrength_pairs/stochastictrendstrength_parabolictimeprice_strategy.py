import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
