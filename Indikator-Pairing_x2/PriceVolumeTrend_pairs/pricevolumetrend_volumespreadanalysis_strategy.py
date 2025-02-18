import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceVolumeTrend_VolumeSpreadAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceVolumeTrend und VolumeSpreadAnalysis
    """
    
    params = (
        ('indicators', {
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            },
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            }
        }),
        ('weights', {
            'PriceVolumeTrend': 1.0,
            'VolumeSpreadAnalysis': 1.0
        })
    )
