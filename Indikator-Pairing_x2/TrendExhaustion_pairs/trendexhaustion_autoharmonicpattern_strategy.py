import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
