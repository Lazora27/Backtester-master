import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
