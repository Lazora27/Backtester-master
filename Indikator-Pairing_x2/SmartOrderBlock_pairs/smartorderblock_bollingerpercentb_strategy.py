import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'BollingerPercentB': 1.0
        })
    )
