import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
