import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'ProjectionBands': 1.0
        })
    )
