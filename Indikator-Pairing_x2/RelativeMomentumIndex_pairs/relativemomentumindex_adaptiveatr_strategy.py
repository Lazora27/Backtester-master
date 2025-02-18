import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
