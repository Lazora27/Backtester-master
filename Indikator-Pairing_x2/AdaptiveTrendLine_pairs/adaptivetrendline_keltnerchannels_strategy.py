import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'KeltnerChannels': 1.0
        })
    )
