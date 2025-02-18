import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
