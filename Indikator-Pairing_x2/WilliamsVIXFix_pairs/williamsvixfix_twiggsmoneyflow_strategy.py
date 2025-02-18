import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsVIXFix_TwiggsMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsVIXFix und TwiggsMoneyFlow
    """
    
    params = (
        ('indicators', {
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            },
            'TwiggsMoneyFlow': {
                'class': TwiggsMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwiggsMoneyFlow'>
            }
        }),
        ('weights', {
            'WilliamsVIXFix': 1.0,
            'TwiggsMoneyFlow': 1.0
        })
    )
