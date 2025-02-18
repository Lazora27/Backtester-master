import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_AutoHarmonicPattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und AutoHarmonicPattern
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'AutoHarmonicPattern': {
                'class': AutoHarmonicPattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoHarmonicPattern'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'AutoHarmonicPattern': 1.0
        })
    )
