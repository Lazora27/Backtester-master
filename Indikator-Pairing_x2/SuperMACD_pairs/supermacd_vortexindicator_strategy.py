import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'VortexIndicator': 1.0
        })
    )
