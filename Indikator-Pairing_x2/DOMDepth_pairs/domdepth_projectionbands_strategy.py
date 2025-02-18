import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'ProjectionBands': 1.0
        })
    )
