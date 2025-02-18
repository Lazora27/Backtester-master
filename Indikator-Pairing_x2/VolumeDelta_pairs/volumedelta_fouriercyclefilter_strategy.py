import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
