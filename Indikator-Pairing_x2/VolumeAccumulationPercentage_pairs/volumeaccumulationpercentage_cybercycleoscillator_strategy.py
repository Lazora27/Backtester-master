import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeAccumulationPercentage_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeAccumulationPercentage und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VolumeAccumulationPercentage': {
                'class': VolumeAccumulationPercentage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeAccumulationPercentage'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'VolumeAccumulationPercentage': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
