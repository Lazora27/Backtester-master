import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
