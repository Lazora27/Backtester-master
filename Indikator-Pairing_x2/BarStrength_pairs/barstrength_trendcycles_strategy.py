import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und TrendCycles
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'TrendCycles': 1.0
        })
    )
