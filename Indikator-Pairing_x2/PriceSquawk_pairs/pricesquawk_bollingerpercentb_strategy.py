import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'BollingerPercentB': 1.0
        })
    )
