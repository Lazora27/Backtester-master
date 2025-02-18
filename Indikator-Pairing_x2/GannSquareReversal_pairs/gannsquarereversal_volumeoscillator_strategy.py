import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'VolumeOscillator': 1.0
        })
    )
