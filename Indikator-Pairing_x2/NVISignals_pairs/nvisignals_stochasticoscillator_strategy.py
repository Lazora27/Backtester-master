import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_StochasticOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und StochasticOscillator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'StochasticOscillator': 1.0
        })
    )
