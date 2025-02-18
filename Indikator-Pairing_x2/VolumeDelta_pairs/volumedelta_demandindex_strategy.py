import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und DemandIndex
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'DemandIndex': 1.0
        })
    )
