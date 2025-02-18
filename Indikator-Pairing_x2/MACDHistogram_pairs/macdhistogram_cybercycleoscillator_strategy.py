import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
