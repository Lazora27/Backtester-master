import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'TRIXIndicator': 1.0
        })
    )
