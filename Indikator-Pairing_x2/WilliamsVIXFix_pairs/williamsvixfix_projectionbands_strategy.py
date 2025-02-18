import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'ProjectionBands': 1.0
        })
    )
