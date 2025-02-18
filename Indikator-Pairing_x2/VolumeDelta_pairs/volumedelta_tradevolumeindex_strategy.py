import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
