import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und MassIndex
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'MassIndex': 1.0
        })
    )
