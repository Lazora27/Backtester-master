import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
