import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'EhlersDecycler': 1.0
        })
    )
