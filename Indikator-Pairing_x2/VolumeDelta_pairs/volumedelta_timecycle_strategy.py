import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und TimeCycle
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'TimeCycle': 1.0
        })
    )
