import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und VWAPBands
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'VWAPBands': 1.0
        })
    )
