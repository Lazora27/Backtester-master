import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'VolumeDelta': 1.0
        })
    )
