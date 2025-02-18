import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PolarizedFractalEfficiency_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PolarizedFractalEfficiency und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PolarizedFractalEfficiency': {
                'class': PolarizedFractalEfficiency,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedFractalEfficiency'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'PolarizedFractalEfficiency': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
