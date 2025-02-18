import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
