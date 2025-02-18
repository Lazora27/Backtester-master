import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
