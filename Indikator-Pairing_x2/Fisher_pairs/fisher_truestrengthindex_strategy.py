import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
