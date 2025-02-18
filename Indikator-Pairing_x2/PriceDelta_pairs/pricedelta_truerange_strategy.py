import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und TrueRange
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'TrueRange': 1.0
        })
    )
