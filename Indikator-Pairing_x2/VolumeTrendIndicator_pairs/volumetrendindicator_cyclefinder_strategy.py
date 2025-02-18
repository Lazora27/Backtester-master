import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_CycleFinder_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und CycleFinder
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'CycleFinder': {
                'class': CycleFinder,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CycleFinder'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'CycleFinder': 1.0
        })
    )
