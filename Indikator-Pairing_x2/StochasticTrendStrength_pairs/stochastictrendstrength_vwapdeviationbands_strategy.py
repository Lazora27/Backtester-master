import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
