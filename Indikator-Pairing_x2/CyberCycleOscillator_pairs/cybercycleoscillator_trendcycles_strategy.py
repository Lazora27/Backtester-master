import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycleOscillator_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycleOscillator und TrendCycles
    """
    
    params = (
        ('indicators', {
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'CyberCycleOscillator': 1.0,
            'TrendCycles': 1.0
        })
    )
