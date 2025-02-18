import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
