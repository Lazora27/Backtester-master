import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und CyberCycle
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'CyberCycle': 1.0
        })
    )
