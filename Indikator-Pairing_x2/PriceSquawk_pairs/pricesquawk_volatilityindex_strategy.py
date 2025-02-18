import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'VolatilityIndex': 1.0
        })
    )
