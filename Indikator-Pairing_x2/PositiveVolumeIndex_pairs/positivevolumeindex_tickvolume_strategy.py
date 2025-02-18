import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_TickVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und TickVolume
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'TickVolume': 1.0
        })
    )
