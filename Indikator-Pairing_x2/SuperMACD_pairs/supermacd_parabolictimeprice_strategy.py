import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
