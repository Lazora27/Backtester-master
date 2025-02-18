import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_NegativeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und NegativeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'NegativeVolumeIndex': 1.0
        })
    )
