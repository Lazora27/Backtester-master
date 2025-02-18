import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedTimePrice_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedTimePrice und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'PolarizedTimePrice': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
