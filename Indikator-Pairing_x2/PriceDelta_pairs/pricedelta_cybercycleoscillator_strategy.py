import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
