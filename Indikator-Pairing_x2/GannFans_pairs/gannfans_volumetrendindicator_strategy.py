import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
