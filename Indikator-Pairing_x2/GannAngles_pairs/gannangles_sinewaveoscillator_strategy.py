import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
