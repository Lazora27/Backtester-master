import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'CyberCycle': 1.0
        })
    )
