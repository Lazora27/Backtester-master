import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
