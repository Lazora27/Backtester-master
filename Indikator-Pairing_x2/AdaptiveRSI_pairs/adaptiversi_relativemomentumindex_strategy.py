import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
