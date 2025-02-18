import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
