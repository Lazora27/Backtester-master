import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
