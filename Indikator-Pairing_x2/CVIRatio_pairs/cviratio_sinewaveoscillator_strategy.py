import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
