import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_PriceSquawk_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und PriceSquawk
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'PriceSquawk': 1.0
        })
    )
