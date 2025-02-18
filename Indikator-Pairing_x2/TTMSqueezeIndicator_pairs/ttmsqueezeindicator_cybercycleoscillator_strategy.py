import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TTMSqueezeIndicator_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TTMSqueezeIndicator und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TTMSqueezeIndicator': {
                'class': TTMSqueezeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TTMSqueezeIndicator'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'TTMSqueezeIndicator': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
