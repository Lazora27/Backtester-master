import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
