import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und CyberCycle
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'CyberCycle': 1.0
        })
    )
