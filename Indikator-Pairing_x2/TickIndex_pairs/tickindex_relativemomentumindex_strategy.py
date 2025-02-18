import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
