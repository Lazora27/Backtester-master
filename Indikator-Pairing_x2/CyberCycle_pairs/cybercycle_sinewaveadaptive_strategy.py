import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CyberCycle_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CyberCycle und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'CyberCycle': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
