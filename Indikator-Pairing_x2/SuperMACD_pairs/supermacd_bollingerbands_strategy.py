import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und BollingerBands
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'BollingerBands': 1.0
        })
    )
