import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
