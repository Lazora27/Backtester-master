import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'TimeCycle': 1.0
        })
    )
