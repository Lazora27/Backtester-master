import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
