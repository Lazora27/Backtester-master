import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NormalizedAverageTrueRange_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NormalizedAverageTrueRange und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'NormalizedAverageTrueRange': {
                'class': NormalizedAverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedAverageTrueRange'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'NormalizedAverageTrueRange': 1.0,
            'BollingerPercentB': 1.0
        })
    )
