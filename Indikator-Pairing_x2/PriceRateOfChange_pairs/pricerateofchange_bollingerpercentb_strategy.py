import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'BollingerPercentB': 1.0
        })
    )
