import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
