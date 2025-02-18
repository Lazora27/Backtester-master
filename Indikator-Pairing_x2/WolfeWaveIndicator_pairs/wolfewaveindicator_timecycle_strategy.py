import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und TimeCycle
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'TimeCycle': 1.0
        })
    )
