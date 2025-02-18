import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
