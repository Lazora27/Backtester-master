import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
