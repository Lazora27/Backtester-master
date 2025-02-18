import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
