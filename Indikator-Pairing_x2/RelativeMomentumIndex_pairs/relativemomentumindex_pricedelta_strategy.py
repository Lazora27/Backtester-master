import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
