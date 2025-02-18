import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
