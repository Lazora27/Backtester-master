import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
