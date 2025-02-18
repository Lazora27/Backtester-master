import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
