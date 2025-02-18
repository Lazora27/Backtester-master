import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
