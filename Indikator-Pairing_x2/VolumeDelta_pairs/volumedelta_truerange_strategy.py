import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und TrueRange
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'TrueRange': 1.0
        })
    )
