import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und GannAngles
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'GannAngles': 1.0
        })
    )
