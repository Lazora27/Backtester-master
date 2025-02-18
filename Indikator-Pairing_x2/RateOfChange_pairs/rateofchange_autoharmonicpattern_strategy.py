import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
