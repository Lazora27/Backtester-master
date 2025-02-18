import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
