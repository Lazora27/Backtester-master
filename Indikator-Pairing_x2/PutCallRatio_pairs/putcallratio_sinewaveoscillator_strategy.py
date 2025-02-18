import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
