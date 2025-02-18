import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_PutCallRatio_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und PutCallRatio
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'PutCallRatio': 1.0
        })
    )
