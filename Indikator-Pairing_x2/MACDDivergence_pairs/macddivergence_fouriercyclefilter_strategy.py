import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
