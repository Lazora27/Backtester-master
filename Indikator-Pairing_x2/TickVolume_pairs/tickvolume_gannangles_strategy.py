import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und GannAngles
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'GannAngles': 1.0
        })
    )
