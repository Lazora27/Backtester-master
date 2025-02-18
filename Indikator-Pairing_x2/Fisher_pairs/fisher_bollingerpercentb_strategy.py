import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'BollingerPercentB': 1.0
        })
    )
