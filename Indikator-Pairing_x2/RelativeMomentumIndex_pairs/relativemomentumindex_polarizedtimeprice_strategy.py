import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
