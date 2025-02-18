import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
