import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NormalizedAverageTrueRange_VolumeSpreadAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NormalizedAverageTrueRange und VolumeSpreadAnalysis
    """
    
    params = (
        ('indicators', {
            'NormalizedAverageTrueRange': {
                'class': NormalizedAverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedAverageTrueRange'>
            },
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            }
        }),
        ('weights', {
            'NormalizedAverageTrueRange': 1.0,
            'VolumeSpreadAnalysis': 1.0
        })
    )
