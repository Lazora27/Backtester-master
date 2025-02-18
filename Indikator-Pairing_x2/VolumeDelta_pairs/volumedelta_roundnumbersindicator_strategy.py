import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
