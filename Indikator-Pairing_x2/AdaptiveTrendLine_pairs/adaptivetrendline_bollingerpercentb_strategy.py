import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'BollingerPercentB': 1.0
        })
    )
