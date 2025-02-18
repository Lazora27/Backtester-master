import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und DemandIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'DemandIndex': 1.0
        })
    )
