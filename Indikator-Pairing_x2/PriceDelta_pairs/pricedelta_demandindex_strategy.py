import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und DemandIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'DemandIndex': 1.0
        })
    )
