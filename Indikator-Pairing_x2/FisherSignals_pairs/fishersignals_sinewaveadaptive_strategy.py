import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
