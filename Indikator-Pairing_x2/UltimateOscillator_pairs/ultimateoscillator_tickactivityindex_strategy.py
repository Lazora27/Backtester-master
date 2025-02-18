import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_TickActivityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und TickActivityIndex
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'TickActivityIndex': 1.0
        })
    )
