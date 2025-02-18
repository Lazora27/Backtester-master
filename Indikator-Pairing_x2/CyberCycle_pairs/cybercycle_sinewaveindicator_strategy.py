import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
