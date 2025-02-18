import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'BollingerPercentB': 1.0
        })
    )
