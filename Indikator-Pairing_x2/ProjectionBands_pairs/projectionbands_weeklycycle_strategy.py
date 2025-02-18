import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'WeeklyCycle': 1.0
        })
    )
