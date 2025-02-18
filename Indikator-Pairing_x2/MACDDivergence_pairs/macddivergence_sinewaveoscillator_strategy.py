import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
