import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
