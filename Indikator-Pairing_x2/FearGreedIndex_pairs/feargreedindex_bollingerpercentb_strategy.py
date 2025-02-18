import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
