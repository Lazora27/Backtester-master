import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'BuyingPressure': 1.0
        })
    )
