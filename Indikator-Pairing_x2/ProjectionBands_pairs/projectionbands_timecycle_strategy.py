import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und TimeCycle
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'TimeCycle': 1.0
        })
    )
