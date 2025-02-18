import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
