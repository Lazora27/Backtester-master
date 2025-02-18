import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'ProjectionBands': 1.0
        })
    )
