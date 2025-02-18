import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
