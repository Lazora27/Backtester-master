import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
