import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'PriceSquawk': 1.0
        })
    )
