import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwiggsMoneyFlow_TPOMarketProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwiggsMoneyFlow und TPOMarketProfile
    """
    
    params = (
        ('indicators', {
            'TwiggsMoneyFlow': {
                'class': TwiggsMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwiggsMoneyFlow'>
            },
            'TPOMarketProfile': {
                'class': TPOMarketProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TPOMarketProfile'>
            }
        }),
        ('weights', {
            'TwiggsMoneyFlow': 1.0,
            'TPOMarketProfile': 1.0
        })
    )
