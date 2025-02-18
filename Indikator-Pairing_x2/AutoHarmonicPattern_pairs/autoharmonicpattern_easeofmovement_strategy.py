import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'EaseOfMovement': 1.0
        })
    )
