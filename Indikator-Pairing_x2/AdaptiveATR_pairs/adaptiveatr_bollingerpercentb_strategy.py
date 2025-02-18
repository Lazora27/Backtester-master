import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'BollingerPercentB': 1.0
        })
    )
