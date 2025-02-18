import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'BollingerPercentB': 1.0
        })
    )
