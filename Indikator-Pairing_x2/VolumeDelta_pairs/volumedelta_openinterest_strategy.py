import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und OpenInterest
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'OpenInterest': 1.0
        })
    )
