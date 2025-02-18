import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
