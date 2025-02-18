import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und TimeCycle
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'TimeCycle': 1.0
        })
    )
