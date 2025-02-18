import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
