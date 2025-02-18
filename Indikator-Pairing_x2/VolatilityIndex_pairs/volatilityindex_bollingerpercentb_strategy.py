import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'BollingerPercentB': 1.0
        })
    )
