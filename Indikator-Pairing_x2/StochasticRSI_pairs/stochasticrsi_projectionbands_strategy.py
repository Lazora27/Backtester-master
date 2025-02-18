import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'ProjectionBands': 1.0
        })
    )
