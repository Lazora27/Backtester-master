import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
