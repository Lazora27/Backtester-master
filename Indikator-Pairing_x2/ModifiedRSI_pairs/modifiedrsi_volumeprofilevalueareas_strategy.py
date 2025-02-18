import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_VolumeProfileValueAreas_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und VolumeProfileValueAreas
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'VolumeProfileValueAreas': {
                'class': VolumeProfileValueAreas,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfileValueAreas'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'VolumeProfileValueAreas': 1.0
        })
    )
