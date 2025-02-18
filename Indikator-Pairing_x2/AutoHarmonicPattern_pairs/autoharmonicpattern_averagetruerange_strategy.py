import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'AverageTrueRange': 1.0
        })
    )
