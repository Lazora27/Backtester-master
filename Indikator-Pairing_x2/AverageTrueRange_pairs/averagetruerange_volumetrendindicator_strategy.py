import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
