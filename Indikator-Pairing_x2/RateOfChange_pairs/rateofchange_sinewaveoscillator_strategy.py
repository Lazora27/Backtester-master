import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
