import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und RateOfChange
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'RateOfChange': 1.0
        })
    )
