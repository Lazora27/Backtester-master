import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FractalChaosOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FractalChaosOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'FractalChaosOscillator': {
                'class': FractalChaosOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FractalChaosOscillator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'FractalChaosOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
