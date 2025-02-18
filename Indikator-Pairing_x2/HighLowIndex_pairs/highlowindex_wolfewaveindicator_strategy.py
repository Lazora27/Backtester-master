import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_WolfeWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und WolfeWaveIndicator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'WolfeWaveIndicator': 1.0
        })
    )
