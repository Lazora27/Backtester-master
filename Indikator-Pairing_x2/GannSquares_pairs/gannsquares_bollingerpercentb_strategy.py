import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'BollingerPercentB': 1.0
        })
    )
