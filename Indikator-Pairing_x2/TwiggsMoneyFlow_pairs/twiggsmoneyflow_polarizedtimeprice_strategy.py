import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwiggsMoneyFlow_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwiggsMoneyFlow und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'TwiggsMoneyFlow': {
                'class': TwiggsMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwiggsMoneyFlow'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'TwiggsMoneyFlow': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
