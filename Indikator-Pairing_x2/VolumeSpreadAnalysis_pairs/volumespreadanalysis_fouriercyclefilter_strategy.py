import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeSpreadAnalysis_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeSpreadAnalysis und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'VolumeSpreadAnalysis': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
