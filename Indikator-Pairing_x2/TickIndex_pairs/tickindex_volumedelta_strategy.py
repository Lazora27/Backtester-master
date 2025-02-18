import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'VolumeDelta': 1.0
        })
    )
