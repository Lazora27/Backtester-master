import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
