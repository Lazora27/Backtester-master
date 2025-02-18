import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
