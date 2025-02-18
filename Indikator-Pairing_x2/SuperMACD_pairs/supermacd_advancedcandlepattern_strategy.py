import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
