import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
