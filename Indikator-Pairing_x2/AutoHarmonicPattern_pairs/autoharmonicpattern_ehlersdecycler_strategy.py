import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'EhlersDecycler': 1.0
        })
    )
