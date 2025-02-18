import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfileValueAreas_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfileValueAreas und CyberCycle
    """
    
    params = (
        ('indicators', {
            'VolumeProfileValueAreas': {
                'class': VolumeProfileValueAreas,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfileValueAreas'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'VolumeProfileValueAreas': 1.0,
            'CyberCycle': 1.0
        })
    )
