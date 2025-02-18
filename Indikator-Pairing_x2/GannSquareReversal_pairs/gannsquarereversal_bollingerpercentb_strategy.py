import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'BollingerPercentB': 1.0
        })
    )
