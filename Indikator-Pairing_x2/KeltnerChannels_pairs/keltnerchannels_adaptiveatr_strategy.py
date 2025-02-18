import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'AdaptiveATR': 1.0
        })
    )
