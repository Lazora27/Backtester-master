import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und SuperMACD
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'SuperMACD': 1.0
        })
    )
