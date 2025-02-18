import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
