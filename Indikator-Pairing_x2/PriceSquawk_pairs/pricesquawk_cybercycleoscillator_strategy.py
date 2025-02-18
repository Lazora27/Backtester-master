import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
