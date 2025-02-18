import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
