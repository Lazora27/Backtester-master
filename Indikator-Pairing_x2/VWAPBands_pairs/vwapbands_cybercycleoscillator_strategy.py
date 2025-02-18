import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
