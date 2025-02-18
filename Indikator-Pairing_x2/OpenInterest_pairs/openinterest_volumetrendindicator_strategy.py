import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
