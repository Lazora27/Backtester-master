import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und TrendCycles
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'TrendCycles': 1.0
        })
    )
