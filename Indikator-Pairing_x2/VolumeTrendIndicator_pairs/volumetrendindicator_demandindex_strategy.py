import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und DemandIndex
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'DemandIndex': 1.0
        })
    )
