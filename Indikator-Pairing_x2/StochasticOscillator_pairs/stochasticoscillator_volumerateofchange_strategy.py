import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
