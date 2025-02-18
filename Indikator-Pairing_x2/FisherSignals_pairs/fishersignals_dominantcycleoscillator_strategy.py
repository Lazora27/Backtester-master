import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherSignals_DominantCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherSignals und DominantCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            },
            'DominantCycleOscillator': {
                'class': DominantCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DominantCycleOscillator'>
            }
        }),
        ('weights', {
            'FisherSignals': 1.0,
            'DominantCycleOscillator': 1.0
        })
    )
