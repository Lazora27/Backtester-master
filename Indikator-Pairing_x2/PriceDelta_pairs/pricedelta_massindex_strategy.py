import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und MassIndex
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'MassIndex': 1.0
        })
    )
