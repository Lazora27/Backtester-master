import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'BuyingPressure': 1.0
        })
    )
