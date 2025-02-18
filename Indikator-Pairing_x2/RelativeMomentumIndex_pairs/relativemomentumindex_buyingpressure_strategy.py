import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeMomentumIndex_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeMomentumIndex und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'RelativeMomentumIndex': {
                'class': RelativeMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeMomentumIndex'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'RelativeMomentumIndex': 1.0,
            'BuyingPressure': 1.0
        })
    )
