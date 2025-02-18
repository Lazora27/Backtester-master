import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
