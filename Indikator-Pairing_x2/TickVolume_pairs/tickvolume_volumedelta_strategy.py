import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'VolumeDelta': 1.0
        })
    )
