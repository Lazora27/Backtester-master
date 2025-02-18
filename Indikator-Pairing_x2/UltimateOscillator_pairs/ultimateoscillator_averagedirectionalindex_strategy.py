import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
