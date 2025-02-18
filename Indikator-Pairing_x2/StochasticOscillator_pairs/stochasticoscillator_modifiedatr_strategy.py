import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'ModifiedATR': 1.0
        })
    )
