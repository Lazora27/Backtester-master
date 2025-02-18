import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VerticalHorizontalFilter_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VerticalHorizontalFilter und VWAPBands
    """
    
    params = (
        ('indicators', {
            'VerticalHorizontalFilter': {
                'class': VerticalHorizontalFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VerticalHorizontalFilter'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'VerticalHorizontalFilter': 1.0,
            'VWAPBands': 1.0
        })
    )
