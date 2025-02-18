import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
