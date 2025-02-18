import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
