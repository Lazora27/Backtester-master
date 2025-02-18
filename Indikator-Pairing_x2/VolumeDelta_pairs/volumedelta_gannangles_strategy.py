import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und GannAngles
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'GannAngles': 1.0
        })
    )
