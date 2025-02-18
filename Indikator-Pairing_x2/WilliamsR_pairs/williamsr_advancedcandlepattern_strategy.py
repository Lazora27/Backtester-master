import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
