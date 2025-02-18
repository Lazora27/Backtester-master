import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
