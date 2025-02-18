import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeProfile_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeProfile und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'VolumeProfile': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
