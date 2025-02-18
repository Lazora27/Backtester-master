import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_VolumeProfileValueAreas_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und VolumeProfileValueAreas
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'VolumeProfileValueAreas': {
                'class': VolumeProfileValueAreas,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfileValueAreas'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'VolumeProfileValueAreas': 1.0
        })
    )
