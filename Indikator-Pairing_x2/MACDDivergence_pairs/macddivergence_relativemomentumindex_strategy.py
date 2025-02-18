import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
