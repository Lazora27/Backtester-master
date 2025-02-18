import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'VolumeDelta': 1.0
        })
    )
