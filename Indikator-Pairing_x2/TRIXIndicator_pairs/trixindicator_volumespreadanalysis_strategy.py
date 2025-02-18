import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_VolumeSpreadAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und VolumeSpreadAnalysis
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'VolumeSpreadAnalysis': 1.0
        })
    )
