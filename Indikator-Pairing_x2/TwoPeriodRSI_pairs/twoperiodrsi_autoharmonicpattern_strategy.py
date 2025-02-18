import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
