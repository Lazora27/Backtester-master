import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'SmoothedCycle': 1.0
        })
    )
