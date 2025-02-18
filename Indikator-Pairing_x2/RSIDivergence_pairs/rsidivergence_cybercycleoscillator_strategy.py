import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
