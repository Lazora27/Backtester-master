import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycleOscillator_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycleOscillator und DPOCycles
    """
    
    params = (
        ('indicators', {
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'CyberCycleOscillator': 1.0,
            'DPOCycles': 1.0
        })
    )
