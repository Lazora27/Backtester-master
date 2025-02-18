import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
