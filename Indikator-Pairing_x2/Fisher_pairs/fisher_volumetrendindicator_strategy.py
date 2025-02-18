import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
