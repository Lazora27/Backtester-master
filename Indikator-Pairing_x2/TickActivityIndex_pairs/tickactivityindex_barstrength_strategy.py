import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'BarStrength': 1.0
        })
    )
