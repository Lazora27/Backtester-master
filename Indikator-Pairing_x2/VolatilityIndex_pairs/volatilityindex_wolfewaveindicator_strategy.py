import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
