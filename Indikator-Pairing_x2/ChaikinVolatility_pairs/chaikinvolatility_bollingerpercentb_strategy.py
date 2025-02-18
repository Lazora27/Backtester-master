import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'BollingerPercentB': 1.0
        })
    )
