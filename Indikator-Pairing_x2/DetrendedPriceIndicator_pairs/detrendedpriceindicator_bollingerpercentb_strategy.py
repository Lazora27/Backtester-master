import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DetrendedPriceIndicator_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DetrendedPriceIndicator und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'DetrendedPriceIndicator': {
                'class': DetrendedPriceIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DetrendedPriceIndicator'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'DetrendedPriceIndicator': 1.0,
            'BollingerPercentB': 1.0
        })
    )
