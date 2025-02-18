import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
