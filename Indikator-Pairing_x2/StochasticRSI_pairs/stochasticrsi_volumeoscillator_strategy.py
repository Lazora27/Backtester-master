import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'VolumeOscillator': 1.0
        })
    )
