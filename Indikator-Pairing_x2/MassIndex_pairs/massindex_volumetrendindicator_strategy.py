import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
