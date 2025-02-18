import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
