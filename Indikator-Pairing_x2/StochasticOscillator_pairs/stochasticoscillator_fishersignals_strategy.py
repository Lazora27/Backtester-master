import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und FisherSignals
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'FisherSignals': 1.0
        })
    )
