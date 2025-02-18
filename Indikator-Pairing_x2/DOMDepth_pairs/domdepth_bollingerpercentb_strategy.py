import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'BollingerPercentB': 1.0
        })
    )
