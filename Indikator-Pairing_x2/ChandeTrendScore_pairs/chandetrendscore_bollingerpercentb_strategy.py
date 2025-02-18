import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'BollingerPercentB': 1.0
        })
    )
