import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketOrderFlow_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketOrderFlow und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'MarketOrderFlow': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
