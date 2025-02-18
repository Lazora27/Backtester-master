import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'HilbertTrendline': 1.0
        })
    )
