import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
