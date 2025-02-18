import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RoundNumbersIndicator_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RoundNumbersIndicator und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'RoundNumbersIndicator': 1.0,
            'BollingerPercentB': 1.0
        })
    )
