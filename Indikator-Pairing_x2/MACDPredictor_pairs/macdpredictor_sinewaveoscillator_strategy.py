import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
