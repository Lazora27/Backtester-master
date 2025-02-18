import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
