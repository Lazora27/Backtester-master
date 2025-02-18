import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
