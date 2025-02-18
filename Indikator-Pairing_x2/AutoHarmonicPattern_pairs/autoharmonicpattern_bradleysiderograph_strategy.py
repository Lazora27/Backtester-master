import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'BradleySiderograph': 1.0
        })
    )
