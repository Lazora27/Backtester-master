import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'UlcerIndex': 1.0
        })
    )
