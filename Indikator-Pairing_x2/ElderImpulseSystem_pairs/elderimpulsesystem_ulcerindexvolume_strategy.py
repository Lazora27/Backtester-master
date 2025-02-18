import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
