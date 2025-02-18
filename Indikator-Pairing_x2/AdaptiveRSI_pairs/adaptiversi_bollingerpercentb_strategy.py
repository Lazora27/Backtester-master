import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'BollingerPercentB': 1.0
        })
    )
