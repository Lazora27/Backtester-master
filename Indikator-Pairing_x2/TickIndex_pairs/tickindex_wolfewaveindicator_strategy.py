import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
