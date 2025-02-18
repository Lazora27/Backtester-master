import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'ProjectionBands': 1.0
        })
    )
