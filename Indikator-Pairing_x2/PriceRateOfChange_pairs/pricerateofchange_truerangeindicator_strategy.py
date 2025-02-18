import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
