import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
