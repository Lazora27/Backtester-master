import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'EhlersDecycler': 1.0
        })
    )
