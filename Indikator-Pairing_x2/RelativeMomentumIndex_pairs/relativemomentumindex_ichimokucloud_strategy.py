import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'IchimokuCloud': 1.0
        })
    )
