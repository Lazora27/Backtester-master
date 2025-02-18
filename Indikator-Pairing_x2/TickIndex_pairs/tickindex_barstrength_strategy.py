import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und BarStrength
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'BarStrength': 1.0
        })
    )
