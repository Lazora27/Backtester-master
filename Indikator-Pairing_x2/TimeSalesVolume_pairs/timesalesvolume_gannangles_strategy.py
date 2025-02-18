import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und GannAngles
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'GannAngles': 1.0
        })
    )
