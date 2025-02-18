import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
