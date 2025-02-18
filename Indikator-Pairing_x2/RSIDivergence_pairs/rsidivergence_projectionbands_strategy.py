import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'ProjectionBands': 1.0
        })
    )
