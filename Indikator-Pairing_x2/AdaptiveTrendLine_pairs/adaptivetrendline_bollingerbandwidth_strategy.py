import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
