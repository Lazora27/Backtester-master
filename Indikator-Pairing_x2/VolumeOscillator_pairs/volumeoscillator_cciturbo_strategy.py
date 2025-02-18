import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeOscillator_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeOscillator und CCITurbo
    """
    
    params = (
        ('indicators', {
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'VolumeOscillator': 1.0,
            'CCITurbo': 1.0
        })
    )
