import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'ModifiedATR': 1.0
        })
    )
