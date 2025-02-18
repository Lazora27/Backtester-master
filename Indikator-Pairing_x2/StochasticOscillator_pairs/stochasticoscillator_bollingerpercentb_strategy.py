import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'BollingerPercentB': 1.0
        })
    )
