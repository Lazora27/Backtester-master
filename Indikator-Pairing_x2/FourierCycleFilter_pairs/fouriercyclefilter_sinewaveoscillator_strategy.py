import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
