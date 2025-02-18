import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
