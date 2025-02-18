import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und VWAPBands
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'VWAPBands': 1.0
        })
    )
