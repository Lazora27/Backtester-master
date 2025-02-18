import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_AroonIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und AroonIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'AroonIndicator': 1.0
        })
    )
