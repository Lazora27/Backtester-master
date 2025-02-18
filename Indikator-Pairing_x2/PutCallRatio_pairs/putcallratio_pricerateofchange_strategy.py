import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
