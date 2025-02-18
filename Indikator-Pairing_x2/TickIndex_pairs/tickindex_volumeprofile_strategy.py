import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'VolumeProfile': 1.0
        })
    )
