import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
