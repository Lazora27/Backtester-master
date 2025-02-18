import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
