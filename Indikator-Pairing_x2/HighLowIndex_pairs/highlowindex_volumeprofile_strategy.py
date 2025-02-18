import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_VolumeProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und VolumeProfile
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'VolumeProfile': {
                'class': VolumeProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeProfile'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'VolumeProfile': 1.0
        })
    )
