import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'AverageLogRange': 1.0
        })
    )
