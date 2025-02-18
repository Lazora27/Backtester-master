import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und GannFans
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'GannFans': 1.0
        })
    )
