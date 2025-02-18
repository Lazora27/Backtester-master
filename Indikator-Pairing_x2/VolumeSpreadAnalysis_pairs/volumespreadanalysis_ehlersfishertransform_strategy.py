import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeSpreadAnalysis_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeSpreadAnalysis und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'VolumeSpreadAnalysis': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
