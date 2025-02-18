import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
