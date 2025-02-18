import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
