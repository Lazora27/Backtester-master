import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
