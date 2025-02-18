import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
