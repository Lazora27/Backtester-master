import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CenterOfGravity_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CenterOfGravity und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'CenterOfGravity': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
