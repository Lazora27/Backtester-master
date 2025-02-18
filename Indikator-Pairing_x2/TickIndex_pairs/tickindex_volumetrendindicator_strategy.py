import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
