import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
