import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'TRIXIndicator': 1.0
        })
    )
