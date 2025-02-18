import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und DPOCycles
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'DPOCycles': 1.0
        })
    )
