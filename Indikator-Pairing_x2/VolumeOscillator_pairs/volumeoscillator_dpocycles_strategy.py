import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'DPOCycles': 1.0
        })
    )
