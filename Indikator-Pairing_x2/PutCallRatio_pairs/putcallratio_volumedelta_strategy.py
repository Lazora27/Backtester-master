import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'VolumeDelta': 1.0
        })
    )
