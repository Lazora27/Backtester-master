import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'ProjectionBands': 1.0
        })
    )
