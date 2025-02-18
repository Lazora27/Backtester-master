import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FourierCycleFilter_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FourierCycleFilter und TrendCycles
    """
    
    params = (
        ('indicators', {
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'FourierCycleFilter': 1.0,
            'TrendCycles': 1.0
        })
    )
