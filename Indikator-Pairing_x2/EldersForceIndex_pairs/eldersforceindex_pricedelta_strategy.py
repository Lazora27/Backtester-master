import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_PriceDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und PriceDelta
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'PriceDelta': 1.0
        })
    )
