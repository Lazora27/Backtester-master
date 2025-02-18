import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
