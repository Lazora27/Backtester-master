import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'BollingerPercentB': 1.0
        })
    )
