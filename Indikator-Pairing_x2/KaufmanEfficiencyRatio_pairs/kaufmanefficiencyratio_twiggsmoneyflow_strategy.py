import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KaufmanEfficiencyRatio_TwiggsMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KaufmanEfficiencyRatio und TwiggsMoneyFlow
    """
    
    params = (
        ('indicators', {
            'KaufmanEfficiencyRatio': {
                'class': KaufmanEfficiencyRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KaufmanEfficiencyRatio'>
            },
            'TwiggsMoneyFlow': {
                'class': TwiggsMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwiggsMoneyFlow'>
            }
        }),
        ('weights', {
            'KaufmanEfficiencyRatio': 1.0,
            'TwiggsMoneyFlow': 1.0
        })
    )
