import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_TwiggsMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und TwiggsMoneyFlow
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'TwiggsMoneyFlow': {
                'class': TwiggsMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwiggsMoneyFlow'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'TwiggsMoneyFlow': 1.0
        })
    )
