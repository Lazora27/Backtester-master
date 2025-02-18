import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBandSqueeze_TwiggsMoneyFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBandSqueeze und TwiggsMoneyFlow
    """
    
    params = (
        ('indicators', {
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            },
            'TwiggsMoneyFlow': {
                'class': TwiggsMoneyFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwiggsMoneyFlow'>
            }
        }),
        ('weights', {
            'BollingerBandSqueeze': 1.0,
            'TwiggsMoneyFlow': 1.0
        })
    )
