import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
