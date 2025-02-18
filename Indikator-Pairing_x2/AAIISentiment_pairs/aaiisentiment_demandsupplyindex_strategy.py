import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AAIISentiment_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AAIISentiment und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'AAIISentiment': {
                'class': AAIISentiment,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AAIISentiment'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'AAIISentiment': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
