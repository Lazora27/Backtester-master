import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'CenterOfGravity': 1.0
        })
    )
