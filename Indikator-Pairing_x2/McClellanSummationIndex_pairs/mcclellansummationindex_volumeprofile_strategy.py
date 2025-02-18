import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'VolumeProfile': 1.0
        })
    )
