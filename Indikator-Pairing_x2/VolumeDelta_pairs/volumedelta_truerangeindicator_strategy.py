import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
