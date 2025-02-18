import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ProjectionBands': 1.0
        })
    )
