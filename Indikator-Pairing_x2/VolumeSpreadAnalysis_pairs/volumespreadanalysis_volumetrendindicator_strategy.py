import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeSpreadAnalysis_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeSpreadAnalysis und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'VolumeSpreadAnalysis': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
