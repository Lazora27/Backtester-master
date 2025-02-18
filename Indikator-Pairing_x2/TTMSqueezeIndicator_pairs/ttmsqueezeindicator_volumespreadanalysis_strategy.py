import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TTMSqueezeIndicator_VolumeSpreadAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TTMSqueezeIndicator und VolumeSpreadAnalysis
    """
    
    params = (
        ('indicators', {
            'TTMSqueezeIndicator': {
                'class': TTMSqueezeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TTMSqueezeIndicator'>
            },
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            }
        }),
        ('weights', {
            'TTMSqueezeIndicator': 1.0,
            'VolumeSpreadAnalysis': 1.0
        })
    )
