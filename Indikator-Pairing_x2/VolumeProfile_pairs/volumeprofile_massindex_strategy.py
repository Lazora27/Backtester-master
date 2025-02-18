import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und MassIndex
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'MassIndex': 1.0
        })
    )
