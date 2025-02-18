import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
