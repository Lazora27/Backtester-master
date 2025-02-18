import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'UltimateOscillator': 1.0
        })
    )
