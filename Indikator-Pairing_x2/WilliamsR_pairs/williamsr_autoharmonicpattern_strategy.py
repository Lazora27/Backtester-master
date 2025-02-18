import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
