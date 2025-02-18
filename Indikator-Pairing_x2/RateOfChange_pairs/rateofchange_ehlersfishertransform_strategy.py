import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
