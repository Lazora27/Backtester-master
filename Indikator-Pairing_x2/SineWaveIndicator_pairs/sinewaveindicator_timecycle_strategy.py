import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SineWaveIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SineWaveIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'SineWaveIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
