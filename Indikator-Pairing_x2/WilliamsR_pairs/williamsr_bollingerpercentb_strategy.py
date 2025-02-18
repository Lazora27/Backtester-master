import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'BollingerPercentB': 1.0
        })
    )
