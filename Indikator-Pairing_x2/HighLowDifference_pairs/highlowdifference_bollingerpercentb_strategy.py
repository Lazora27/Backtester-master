import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'BollingerPercentB': 1.0
        })
    )
