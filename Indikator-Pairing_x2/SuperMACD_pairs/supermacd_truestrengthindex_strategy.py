import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
