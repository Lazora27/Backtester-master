import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_VolumeProfileValueAreas_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und VolumeProfileValueAreas
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'VolumeProfileValueAreas': {
                'class': VolumeProfileValueAreas,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfileValueAreas'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'VolumeProfileValueAreas': 1.0
        })
    )
