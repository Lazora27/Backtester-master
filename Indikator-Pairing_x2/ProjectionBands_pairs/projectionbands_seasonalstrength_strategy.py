import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ProjectionBands_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ProjectionBands und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'ProjectionBands': 1.0,
            'SeasonalStrength': 1.0
        })
    )
