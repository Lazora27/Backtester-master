import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'ProjectionBands': 1.0
        })
    )
