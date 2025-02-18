import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und VWAPBands
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'VWAPBands': 1.0
        })
    )
