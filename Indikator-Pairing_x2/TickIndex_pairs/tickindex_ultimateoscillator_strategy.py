import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_UltimateOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und UltimateOscillator
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'UltimateOscillator': 1.0
        })
    )
