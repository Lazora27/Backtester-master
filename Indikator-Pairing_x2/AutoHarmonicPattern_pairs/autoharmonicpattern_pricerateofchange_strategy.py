import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoHarmonicPattern_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoHarmonicPattern und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'AutoHarmonicPattern': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
