import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ProjectionBands': 1.0
        })
    )
