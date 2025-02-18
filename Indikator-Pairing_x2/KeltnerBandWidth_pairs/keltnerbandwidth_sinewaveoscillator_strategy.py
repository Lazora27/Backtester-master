import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerBandWidth_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerBandWidth und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'KeltnerBandWidth': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
