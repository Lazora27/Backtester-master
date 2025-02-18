import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
