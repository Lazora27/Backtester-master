import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeTrendIndicator_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeTrendIndicator und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'VolumeTrendIndicator': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
