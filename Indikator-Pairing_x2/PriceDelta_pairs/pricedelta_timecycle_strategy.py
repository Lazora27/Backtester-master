import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und TimeCycle
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'TimeCycle': 1.0
        })
    )
