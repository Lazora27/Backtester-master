import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_KeltnerChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und KeltnerChannels
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'KeltnerChannels': 1.0
        })
    )
