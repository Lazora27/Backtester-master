import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und DemandIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'DemandIndex': 1.0
        })
    )
