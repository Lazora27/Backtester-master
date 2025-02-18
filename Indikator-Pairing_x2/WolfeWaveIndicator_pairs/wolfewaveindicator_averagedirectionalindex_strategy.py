import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
