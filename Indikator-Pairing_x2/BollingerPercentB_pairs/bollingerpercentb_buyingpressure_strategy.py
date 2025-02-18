import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'BuyingPressure': 1.0
        })
    )
