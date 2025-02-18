import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_TimeSalesVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und TimeSalesVolume
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'TimeSalesVolume': 1.0
        })
    )
