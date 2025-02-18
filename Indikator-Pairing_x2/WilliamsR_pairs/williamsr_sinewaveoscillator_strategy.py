import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
