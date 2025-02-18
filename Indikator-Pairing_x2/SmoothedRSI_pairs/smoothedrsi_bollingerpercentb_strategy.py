import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'BollingerPercentB': 1.0
        })
    )
