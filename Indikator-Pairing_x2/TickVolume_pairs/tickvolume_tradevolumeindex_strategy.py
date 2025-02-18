import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
