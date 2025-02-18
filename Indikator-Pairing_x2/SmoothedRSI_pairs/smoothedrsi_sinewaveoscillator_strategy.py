import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
