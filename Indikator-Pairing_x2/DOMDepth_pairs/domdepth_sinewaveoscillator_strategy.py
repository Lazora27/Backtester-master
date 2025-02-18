import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
