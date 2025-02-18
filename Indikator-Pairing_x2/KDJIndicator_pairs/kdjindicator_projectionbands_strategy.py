import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'ProjectionBands': 1.0
        })
    )
