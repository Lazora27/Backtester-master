import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
