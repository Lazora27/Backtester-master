import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und MassIndex
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'MassIndex': 1.0
        })
    )
