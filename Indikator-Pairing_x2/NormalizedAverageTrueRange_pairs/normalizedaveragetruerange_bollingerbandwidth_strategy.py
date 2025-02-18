import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NormalizedAverageTrueRange_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NormalizedAverageTrueRange und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'NormalizedAverageTrueRange': {
                'class': NormalizedAverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedAverageTrueRange'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'NormalizedAverageTrueRange': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
