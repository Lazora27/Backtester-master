import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'VolumeOscillator': 1.0
        })
    )
