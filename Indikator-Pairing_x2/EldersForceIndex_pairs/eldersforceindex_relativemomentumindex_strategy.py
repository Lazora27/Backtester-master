import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_RelativeMomentumIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und RelativeMomentumIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'RelativeMomentumIndex': 1.0
        })
    )
