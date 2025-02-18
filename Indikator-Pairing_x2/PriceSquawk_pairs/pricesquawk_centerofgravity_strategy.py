import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'CenterOfGravity': 1.0
        })
    )
