import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BuyingPressure_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BuyingPressure und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'BuyingPressure': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
