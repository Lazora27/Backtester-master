import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
