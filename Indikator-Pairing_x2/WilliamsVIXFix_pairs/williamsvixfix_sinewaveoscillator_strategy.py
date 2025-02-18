import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
