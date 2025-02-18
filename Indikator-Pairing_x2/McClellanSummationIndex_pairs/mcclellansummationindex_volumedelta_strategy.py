import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'VolumeDelta': 1.0
        })
    )
